import os
from glob import glob


'''Merge text files.'''


def merger():

    contents = []
    for file in sorted(glob(os.path.join('tmp', '*.txt'))):
        with open(file, 'r', encoding='utf-8') as file:
            contents.append(file.read())
    with open(os.path.join('tmp', 'mfile.txt'), 'w', encoding='utf-8') as mfile:
        for content in contents:
            mfile.write(content + '\n')
    print('File merge complete.')


if __name__ == '__main__':
    merger()
