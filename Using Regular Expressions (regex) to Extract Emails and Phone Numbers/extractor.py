'''Extract the email addresses and phone numbers from a piece of text.'''


import re
import os


def extractor():
    '''Email and phone number extractor function'''

    path = os.path.join('tmp', 'text.txt')

    phone_pattern = re.compile(r'\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{4}')
    email_pattern = re.compile(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            phone_numbers = phone_pattern.findall(content)
            emails = email_pattern.findall(content)
            print(phone_numbers)
            print(emails)
    else:
        print('The file does not exists.')


if __name__ == '__main__':
    extractor()
