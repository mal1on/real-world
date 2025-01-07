'''Batch-rename the files of a directory.'''


from os import rename, listdir, path
from datetime import date


def renamer(directory='tmp'):
    '''Batch-renames the files of a directory.'''

    if not path.exists(directory):
        print(f'Directory {directory} does not exist.')
        return

    today = date.today()
    for file in listdir(directory):
        file_path = path.join(directory, file)
        if path.isfile(file_path):
            name, ext = path.splitext(file)
            new_name = f'{name}-{today}{ext}'
            new_path = path.join(directory, new_name)
            try:
                rename(file_path, new_path)
            except Exception as e:
                print(f'Error renaming {file_path}: {e}')
    print(f'All files in {directory} directory renamed')


if __name__ == '__main__':
    renamer()
