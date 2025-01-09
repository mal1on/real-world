'''
Create a graph using the matploblib data visualization library and data
from text files.
'''


import os
import matplotlib.pyplot as plt


def plotter(x_axis, y_axis):
    '''Plotter function.'''

    plt.plot(x_axis, y_axis, marker='o', linestyle='-')
    plt.xlabel('File name')
    plt.ylabel('Number')
    plt.title('Numbers from text files')
    plt.grid(True)
    plt.show()


def main(path='tmp'):
    '''Main function.'''

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
        print(f'Path {path} does not exist.')

    plotter(x, y)


if __name__ == '__main__':
    main()
