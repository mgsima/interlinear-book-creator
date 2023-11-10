import subprocess
import pdfkit

def html_to_pdf(input_html, output_pdf):
    options = {
        'page-size': 'A5',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [('Accept-Encoding', 'gzip')]
    }

    pdfkit.from_file(input_html, output_pdf, options=options)

## CONVERSION OF FORMAT OF BOOKS ##
def convert_book(input_path: str, output_path: str):
    '''
    Convert an e-book from one format to another.

    Args:
    - input_path (str): Path to the input file to be converted.
    - output_path (str): Path and name of the output file with the desired extension to determine the output format.

    Note:
    The conversion is done using Calibre's "ebook-convert" tool. 
    Make sure you have Calibre installed and that "ebook-convert" is in the system PATH.
    '''
    subprocess.call(["ebook-convert", input_path, output_path])

