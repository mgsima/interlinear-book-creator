# Interlinear Book Generator

## Project Overview
This tool generates interlinear books, ideal for language learners desiring to read literature in its original language with an accompanying line-by-line translation.

## Features
- Extracts unique words from a `.txt` file containing the original book.
- Translates words and stores them in a PostgreSQL database.
- Generates an interlinear HTML file with the original text and translations.
- Optional conversion of the HTML file to an ebook format (e.g., `.azw3`).

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL installed and running on your local machine.
- An API key for DeepL API for translations.
- The original book in a `.txt` format.

### Database Setup
Before running the script, set up a PostgreSQL database:
1. Install PostgreSQL and create a database named `interlinear_dictionary`.
2. Create a table named `dict` with the fields `word` (text type) and `translation` (text type).
3. Ensure that your database user has the necessary permissions to perform CRUD operations on the database.

### Environment Configuration
You need to set the following environment variables:
- `DEEPL_AUTH_KEY`: Your DeepL API authentication key for translation services.
- `DATABASE_PASSWORD`: The password for your PostgreSQL database user.

You can set these variables in your environment, or use a `.env` file and a library like `python-dotenv` to load them.

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/mgsima/interlinear-book-creator.git
   ```
2. Navigate to the project directory and install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the script, run the following command in the terminal:
```
python interlinear_book.py [path-to-your-text-file]
```
Replace `[path-to-your-text-file]` with the relative or absolute path to your `.txt` file.

## Built With
- Python - The programming language used.
- PostgreSQL - Database system used for storing translations.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
