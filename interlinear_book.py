
from modules.database import connect_to_db, insert_single_word, insert_several_words, abrir_diccionario
from modules.text_processing import extract_unique_words, format_word
from modules.translation import translate_words
from modules.ebook_conversion import convert_book, html_to_pdf
import os
import sys
import argparse
from contextlib import closing


##########################
## CREATING THE BOOK #####
##########################

# Creamos el documento HTML
def interlineate(file_path, dictionary, full_input):  
    '''
    Function that receives the path to a book file, a dictionary containing the book's words, 
    and the path for the output HTML file. The words from the book are matched with their 
    formatted versions as found in the dictionary, so these two must correspond.
    '''
    
    # Convert the dictionary to a set for faster lookups
    keys = set(dictionary)

    # Pre-compile the HTML template for ruby text annotations
    ruby_template = '<ruby><rb>{word}&nbsp;</rb><rt>{translation}</rt></ruby>'

    # Initialize a list to store lines for the HTML output
    output_lines = [
        '<!DOCTYPE html>',
        '<html>',
        '<head>',
        '<style>',
        'ruby { ruby-position: under; }',
        'rt { font-family: verdana; color: darkgray; }',
        'rb { font-family: verdana; color: black; }',
        '</style>',
        '</head>',
        '<body>',
    ]

    # Open the book to be translated
    with open(file_path, 'r', encoding='utf8') as textfile:  
        # Iterate through each line of the file
        for line in textfile:  
            words = line.split()
            line_output = []

            # Process each word in the line
            for w in words:
                # Format the word to strip unwanted characters before and after
                word = format_word(w)  

                # Create the interlinear translation
                if word in keys:  # If the word is in the dictionary, add its translation
                    translation = dictionary[word]
                else:
                    # If the word is not in the dictionary, print a message and leave a blank translation
                    if word:
                        print(f'{word} is not in dictionary')
                    translation = " "

                # Use the pre-compiled template with the original word and its translation
                line_output.append(ruby_template.format(word=w, translation=translation))
            
            # Add the line with interlinear translations to the output lines
            output_lines.append(' '.join(line_output) + '<br />')

    # Add the closing tags of the HTML document to the output lines
    output_lines.extend(['</body>', '</html>'])

    # Write all the content to the output HTML file
    with open(full_input, 'w', encoding='utf8') as output:
        output.write('\n'.join(output_lines))




def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a .txt file and generate an interlinear book.")
    parser.add_argument('file_path', type=str, help='Path to the input .txt file')
    return parser.parse_args()

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist!")
    else:
        return arg

def process_file(file_path):
    root, extension = os.path.splitext(file_path)
    if extension.lower() != '.txt':
        raise ValueError(f"File must be a .txt file. Invalid file {file_path}")
    
    filename = os.path.basename(root)
    return filename, file_path

def main():
    args = parse_arguments()
    file_path = is_valid_file(args, args.file_path)
    filename, file_path = process_file(file_path)

    full_input = filename + ".html"
    full_output = filename + ".azw3"
    pdf_output = filename + '.pdf'

    with closing(connect_to_db()) as conn:  # Ensures that the connection is closed
        unique_word_list = extract_unique_words(file_path)
        missed_words, dict_words = abrir_diccionario(conn, unique_word_list)
        
        if missed_words:
            dictionary, new_words = translate_words(missed_words, dict_words)
            insert_several_words(conn, new_words)
        else:
            dictionary = dict_words
        
        interlineate(file_path, dictionary, full_input)

    # convert_book(full_input, full_output)  # Uncomment if conversion is required
    html_to_pdf(full_output, pdf_output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
