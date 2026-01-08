"""
Search and find content inside PDF files with Python and pdfplumber
"""

from pathlib import Path
import pdfplumber

PDF_DIR = Path('pdfs')

def get_pdfs(directory):
    """Get all pdf files function"""

    return list(directory.glob('*.pdf'))


def finder(word, directory):
    """
    Return name and page number of pdf file/s where a <word> is found
    """
    results = []
    for pdf in get_pdfs(directory):
        with pdfplumber.open(pdf) as doc:
            for page in doc.pages:
                text = page.extract_text()
                if text and word.lower() in text.lower():
                    results.append((str(pdf), page.page_number))

    return results


if __name__ == '__main__':
    word = input('Enter the word you want to search: ')
    results = finder(word, PDF_DIR)
    if results:
        for file_path, page_number in results:
            print(f'{word} was found in: {file_path}, page number: {page_number}')
    else:
        print(f'{word} was not found in {PDF_DIR}')
