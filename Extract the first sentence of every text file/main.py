'''
Script that extracts and prints out the first sentence of each text file.
'''


import re
import os


def get_first_sentence(text):
    '''Function to get the first sentence'''

    pattern = r'[A-Z][^\.!\?]*[\.\!\?]'
    sentence = re.match(pattern, text)

    return sentence.group(0)


get_first_sentence()
