from sklearn.externals import joblib


def save_classifier(classifier_model, file_name):
    directory = 'classifier_dump/'
    extenstion = '.sav'
    save_path = directory + file_name + extenstion

    joblib.dump(classifier_model, save_path)


def load_classifier(file_name):
    directory = 'mining_analysis_tool/classifier_dump/'
    extension = '.sav'
    load_path = directory + file_name + extension

    return joblib.load(load_path)
