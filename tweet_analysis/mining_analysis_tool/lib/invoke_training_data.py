import pandas as pd

from . import data_cleansing
from . import data_importer
from . import data_moulder


def invoke_data():
    # sentiment database - imdb
    data_path = r'C:\Users\Felipe\Documents\Programação\ADS\Projeto de Análise de Dados\Analise_de_sentimentos\Proposta_1\sentiment_dataset\sentiment_labelled_sentences\imdb_labelled.txt'
    class_column = 'class'
    text_column = 'text'

    col_names = [text_column, class_column]

    # Training data.
    train_data_normal = data_importer.import_txt_table_file(data_path, col_names)
    # train_data.head()

    # Training data negation.
    train_data_negation = data_importer.import_txt_table_file(data_path, col_names)

    # Cleaning data text corpus.
    data_cleansing.data_text_cleansing(train_data_normal, text_column)
    data_cleansing.data_text_cleansing(train_data_negation, text_column)

    # Negating data.
    data_moulder.data_text_negation(train_data_negation, text_column)

    databases = [train_data_normal, train_data_negation]

    # Contatenating data and data negation.
    train_data = pd.concat(databases)

    return [train_data, text_column, class_column]
