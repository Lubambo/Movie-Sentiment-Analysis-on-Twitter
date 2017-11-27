from . import text_cleaner


# Data text cleansing.
def data_text_cleansing(data, text_column):
    for row in range(data.shape[0]):
        cell_text = data.loc[row, text_column]
        text = text_cleaner.text_cleansing(cell_text)

        data.set_value(row, text_column, text)
