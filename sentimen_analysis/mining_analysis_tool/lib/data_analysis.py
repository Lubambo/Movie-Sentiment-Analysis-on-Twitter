from . import classifier
from . import data_importer
from . import invoke_classifier


# Analyse the input data and update the given dictionary.
def analyse_data(web_data, summary_dict):
    try:
        clf = invoke_classifier.load_classifier('multinomialNB')

        reviews_column = 'REVIEWS'

        try:
            text_data = data_importer.open_python_list_data(web_data, [reviews_column])

            for text in text_data[reviews_column]:
                # print("text: " + str(text))
                classifier.predict_text(text, summary_dict, clf)
        except:
            print("DATA FILE DOES NOT EXIST.")

    except:
        print("CLASSIFIER FILE DOES NOT EXIST.")
