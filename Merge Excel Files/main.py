'''Merge Excel files'''


import os
import pandas as pd


directory = 'tmp'
output = os.path.join(directory, 'merged_excel.xlsx')


def main():
    '''Main function'''

    if os.path.exists(directory):
        files = os.listdir(directory)
        dfs = []
        for file in files:
            try:
                path = os.path.join(directory, file)
                df = pd.read_excel(path)
                dfs.append(df)
            except ValueError:
                print(f'{file} is not an Excel file. Skipping it.')
        if dfs:
            merged_dfs = pd.concat(dfs, ignore_index=True)
            merged_dfs.to_excel(output, index=False)
            print(f'Existing Excel files merged to merged_excel.xlsx')
    else:
        print(f'Directory {directory} does not exist')


if __name__ == '__main__':
    main()
