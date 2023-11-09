import subprocess

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

