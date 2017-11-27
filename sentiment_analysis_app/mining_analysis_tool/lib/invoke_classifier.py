from sklearn.externals import joblib


def load_classifier(file_name):
    directory = 'mining_analysis_tool/movie_classifier/'
    extension = '.sav'
    load_path = directory + file_name + extension

    return joblib.load(load_path)
