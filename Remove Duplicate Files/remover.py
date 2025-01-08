'''Python script that looks in a folder and removes duplicate files.'''


import os
import hashlib


def file_hash(file):
    '''Calculates file hash.'''

    hash_object = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hash_object.update(data)
    return hash_object.hexdigest()


def main():
    '''
    Python script that looks in a folder and removes duplicate
    files.
    '''

    folder = 'tmp'
    files = sorted(os.listdir(folder))

    if not files:
        print(f'The "{folder}" folder is empty. Nothing to remove.')
        return

    unique = []

    for file in files:
        path = os.path.join(folder, file)
        fhash = file_hash(path)
        if fhash not in unique:
            unique.append(fhash)
        else:
            os.remove(path)
            print(f'{file} is deleted as a duplicate.')


if __name__ == '__main__':
    main()
