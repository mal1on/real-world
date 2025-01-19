'''
Script that looks inside a directory and removes all duplicate pictures
of that directory.
'''


import os
import imagehash
import PIL


directory = 'tmp'


def main():
    '''Main function'''

    image_hashes = []

    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            path = os.path.join(directory, file)
            try:
                image = PIL.Image.open(path)
                image_hash = imagehash.average_hash(image)
                if image_hash in image_hashes:
                    os.remove(path)
                    print(f'{file} is a duplicate. Removing it.')
                else:
                    image_hashes.append(image_hash)
            except PIL.UnidentifiedImageError:
                print(f'{file} is not an image file. Skipping it.')



if __name__ == '__main__':
    main()
