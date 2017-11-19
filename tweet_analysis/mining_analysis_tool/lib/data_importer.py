import codecs
import json

import pandas as pd
import numpy as np


#####################
# Open JSON data. ###
#####################
def open_json_data(data_path):
    data = []

    with codecs.open(data_path, 'rU', 'utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    json_data = pd.DataFrame(data)
    # json_data.head()

    return json_data


####################
# Open CSV data. ###
####################
def open_csv_data(data_path, column_names=[], separator=''):
    if len(column_names) > 0:
        if separator != '':
            csv_data = pd.read_csv(data_path, names=column_names, sep=separator)
        else:
            csv_data = pd.read_csv(data_path, names=column_names)
    else:
        if separator != '':
            csv_data = pd.read_csv(data_path, sep=separator)
        else:
            csv_data = pd.read_csv(data_path)

    # csv_data.head()
    return csv_data


#####################
# Open XLSX data. ###
#####################
def open_xlsx_data(data_path):
    xlsx_data = pd.read_excel(data_path)
    # xlsx_data.head()

    return xlsx_data


####################
# Open tab data. ###
####################
def open_tab_data(data_path):
    tab_data = pd.read_table(data_path, encoding='latin1')
    # tab_data.head()

    return tab_data


def import_txt_table_file(data_path, col_names):
    if len(col_names) > 0:
        data = pd.read_table(data_path, names=col_names, header=None)
    else:
        data = pd.read_table(data_path)

    return data


############################################
# Make a DataFrame out of a python list. ###
############################################
def open_python_list_data(list_data, col_names):
    rows = len(list_data)
    np_data = np.array(list_data).reshape(-1, 1)    #Transform python list into a rowsx1 numpy array.
    return pd.DataFrame(np_data, columns=col_names)
