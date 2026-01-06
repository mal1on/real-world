import pandas as pd


def converter():
    """Convert an Excel file to a CSV file."""


    df = pd.read_excel('tmp/europe.xlsx')
    df.to_csv('tmp/europe.csv', index=False)
