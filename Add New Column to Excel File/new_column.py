import pandas as pd


'''
Python program that alters an Excel file by adding a new column to it.
'''


def add_column():

    df = pd.read_excel('tmp/Input.xlsx')
    df['Total'] = df['Price'] * df['Quantity']
    print(f'New column "Total" added to the data frame.')
    df.to_excel('tmp/output.xlsx', index=False)
    print('New output.xlsx file saved successfully.')


if __name__ == '__main__':
    add_column()
