from . import counterVect_multinomialNB as cmb
from . import data_importer
from . import save_and_load_classifier


def get_web_data(web_data_path, reviews_column):
    web_data = data_importer.open_csv_data(web_data_path, [reviews_column], '\n')
    # print(web_data)

    return web_data


def analyse_data(web_data, summary_dict):
    try:
        clf = save_and_load_classifier.load_classifier('multinomialNB')

        reviews_column = 'REVIEWS'

        try:
            text_data = data_importer.open_python_list_data(web_data, [reviews_column])

            for text in text_data[reviews_column]:
                # print("text: " + str(text))
                cmb.predict_text(text, summary_dict, clf)
        except:
            print("DATA FILE DOES NOT EXIST.")

    except:
        print("CLASSIFIER FILE DOES NOT EXIST.")
