import pandas as pd
import numpy as np

'''
    Converting Series' index into a column in a dataframe
'''

if __name__ == '__main__':
    li = list('abcdefghijklmnopqrstuvwxyz')
    np_array = np.arange(26)
    dictionary = dict(zip(li, np_array))

    series = pd.Series(dictionary)

    df = series.to_frame().reset_index()

    print(df.head())
    