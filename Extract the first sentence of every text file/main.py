'''
Script that extracts and prints out the first sentence of each text file.
'''


import re
import os


directory = 'tmp'


def get_first_sentence(text):
    '''Function to get the first sentence'''

    pattern = r'[A-Z][^.!?\n]+[\.\!\?]'
    match = re.search(pattern, text)

    return match.group() if match else None


def main():
    '''Main function'''

    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            path = os.path.join(directory, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    sentence = get_first_sentence(f.read())
                    if sentence:
                        print(sentence)
            except Exception as e:
                print(f'Error opening {file}: {e}')
    else:
        print(f'{directory} does not exist')


if __name__ == '__main__':
    main()
