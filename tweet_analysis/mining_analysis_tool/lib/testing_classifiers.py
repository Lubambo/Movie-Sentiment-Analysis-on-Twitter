import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split


gr_headers = ['Features', 'Vectorizer', 'Classifier', 'False Neg', 'False Pos', 'F1']
global_results = dict()


def testing_classifiers(data, text_column, class_column):
    scores = []
    confusion = []

    # Pipe1
    bwc_mn_nb = bwc_mnnb()
    parcial_res_1 = dict()
    scores_res_1 = []
    confusion_1 = np.array([[0, 0], [0, 0]])

    # Pipe2
    bgc_mn_nb = bgc_mnnb()
    parcial_res_2 = dict()
    scores_res_2 = []
    confusion_2 = np.array([[0, 0], [0, 0]])

    # Pipe3
    bgf_mn_nb = bgf_mnnb()
    parcial_res_3 = dict()
    scores_res_3 = []
    confusion_3 = np.array([[0, 0], [0, 0]])

    # Pipe4
    bgo_bl_nb = bgo_blnb()
    parcial_res_4 = dict()
    scores_res_4 = []
    confusion_4 = np.array([[0, 0], [0, 0]])

    # Pipe5
    bgf_bl_nb = bgf_blnb()
    parcial_res_5 = dict()
    scores_res_5 = []
    confusion_5 = np.array([[0, 0], [0, 0]])

    scores.append(scores_res_1)
    scores.append(scores_res_2)
    scores.append(scores_res_3)
    scores.append(scores_res_4)
    scores.append(scores_res_5)

    confusion.append(confusion_1)
    confusion.append(confusion_2)
    confusion.append(confusion_3)
    confusion.append(confusion_4)
    confusion.append(confusion_5)

    k_fold = KFold(n=len(data), n_folds=10)


    for train_indices, test_indices in k_fold:
        # Gathering Train folds.
        train_text = data.iloc[train_indices][text_column].values
        train_y = data.iloc[train_indices][class_column].values

        # Gathering Test folds
        test_text = data.iloc[test_indices][text_column].values
        test_y = data.iloc[test_indices][class_column].values

        calculate_results(bwc_mn_nb[3], confusion[0], scores[0], train_text, train_y, test_text, test_y)
        calculate_results(bgc_mn_nb[3], confusion[1], scores[1], train_text, train_y, test_text, test_y)
        calculate_results(bgf_mn_nb[3], confusion[2], scores[2], train_text, train_y, test_text, test_y)
        calculate_results(bgo_bl_nb[3], confusion[3], scores[3], train_text, train_y, test_text, test_y)
        calculate_results(bgf_bl_nb[3], confusion[4], scores[4], train_text, train_y, test_text, test_y)

    update_parcial_results(parcial_res_1, bwc_mn_nb, confusion[0], scores[0])
    update_parcial_results(parcial_res_2, bgc_mn_nb, confusion[1], scores[1])
    update_parcial_results(parcial_res_3, bwc_mn_nb, confusion[2], scores[2])
    update_parcial_results(parcial_res_4, bgo_bl_nb, confusion[3], scores[3])
    update_parcial_results(parcial_res_5, bgf_bl_nb, confusion[4], scores[4])

    results_list = []
    results_list.append(parcial_res_1)
    results_list.append(parcial_res_2)
    results_list.append(parcial_res_3)
    results_list.append(parcial_res_4)
    results_list.append(parcial_res_5)

    for i in range(len(results_list)):
        print("Features: " + results_list[i][gr_headers[0]])
        print("Vectorizer: " + results_list[i][gr_headers[1]])
        print("Classifier: " + results_list[i][gr_headers[2]])
        print("False Neg: " + str(results_list[i][gr_headers[3]]))
        print("False Pos: " + str(results_list[i][gr_headers[4]]))
        print("F1 Score: " + str(results_list[i][gr_headers[5]]))
        print()
        print()


def calculate_results(pipeline, confusion, scores, train_text, train_y, test_text, test_y):
    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)

    score = f1_score(test_y, predictions, pos_label=0)
    scores.append(score)


def update_parcial_results(parcial_res, pipe_info, confusion, f1_scores):
    parcial_res[gr_headers[0]] = pipe_info[0]
    parcial_res[gr_headers[1]] = pipe_info[1]
    parcial_res[gr_headers[2]] = pipe_info[2]
    parcial_res[gr_headers[3]] = confusion[0, 1]
    parcial_res[gr_headers[4]] = confusion[1, 0]
    parcial_res[gr_headers[5]] = sum(f1_scores) / len(f1_scores)

# BWC: Bag of Words Counts
# MNNB: MultinomialNB
def bwc_mnnb():
    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    pipe_info = ["Bag of Words counts", "CountVectorizer", "MultinomialNB", pipeline]

    return pipe_info


# BGC: Bigrams Counts
# MNNB: MultinomialNB
def bgc_mnnb():
    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
        ('classifier', MultinomialNB())
    ])

    pipe_info = ["Bigrams counts", "CountVectorizer", "MultinomialNB", pipeline]

    return pipe_info


# BGF: Bigrams Frequencies
# MNNB: MultinomialNB
def bgf_mnnb():
    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
        ('tfidf_transformer', TfidfTransformer()),
        ('classifier', MultinomialNB())
    ])

    pipe_info = ["Bigrams counts", "CountVectorizer / TfidfTransformer", "MultinomialNB", pipeline]

    return pipe_info


# BGO: Bigrams Occurrences
# BLNB: BernoulliNB
def bgo_blnb():
    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
        ('classifier', BernoulliNB(binarize=0.0))
    ])

    pipe_info = ["Bigrams occurrences", "CountVectorizer", "BernoulliNB", pipeline]

    return pipe_info


# BGF: Bigrams Frequencies
# BLNB: BernoulliNB
def bgf_blnb():
    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
        ('tfidf_transformer', TfidfTransformer()),
        ('classifier', BernoulliNB(binarize=0.0))
    ])

    pipe_info = ["Bigrams occurrences", "CountVectorizer / TfidfTransformer", "BernoulliNB", pipeline]

    return pipe_info