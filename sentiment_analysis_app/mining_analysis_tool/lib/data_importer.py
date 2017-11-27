import pandas as pd
import numpy as np


# Make a DataFrame out of a python list.
def open_python_list_data(list_data, col_names):
    np_data = np.array(list_data).reshape(-1, 1)    #Transform python list into a rowsx1 numpy array.
    return pd.DataFrame(np_data, columns=col_names)
