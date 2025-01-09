'''
Create a graph using the Streamlit data visualization library and data
from text files.
'''


import os
import pandas as pd
import streamlit as st


def plotter(x_axis, y_axis):
    '''Plotter function to create a line chart.'''

    df = pd.DataFrame({'x': x_axis, 'y': y_axis})
    st.title('Numbers from Text Files')
    st.line_chart(df, x='x', y='y', x_label='Files', y_label='Numbers')


def main(path='tmp'):
    '''Main function to read data from files and plot it.'''

    x, y = [], []
    if os.path.exists(path):
        files = sorted(os.listdir(path))
        for file in files:
            name = os.path.splitext(file)[0]
            x.append(name)
            file_path = os.path.join(path, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                y.append(float(f.read()))
    else:
        st.error(f'Path {path} does not exist.')

    plotter(x, y)


if __name__ == '__main__':
    main()
