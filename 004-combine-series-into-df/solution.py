import pandas as pd
import numpy as np

if __name__ == "__main__":
    series_1 = pd.Series(np.arange(10))
    series_2 = pd.Series(list('ABCDEFGHIJ'))

    df = pd.concat([series_1, series_2], axis=1)

    print(df.head())