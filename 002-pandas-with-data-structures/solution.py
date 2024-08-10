import pandas as pd
import numpy as np

'''
    Using Pandas library with lists,
    numpy array, and dictionaries
'''

if __name__ == '__main__':
    li = list('abcdefghijklmnopqrstuvwxyz')
    np_array = np.arange(26)
    dictionary = dict(zip(li, np_array))

    li_series = pd.Series(li)
    numpy_series = pd.Series(np_array)
    dict_series = pd.Series(dictionary)

    print('List series:\n', li_series)
    print('Numpy series:\n', numpy_series)
    print('Dict series:\n', dict_series)