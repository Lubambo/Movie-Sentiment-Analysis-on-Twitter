import numpy as np

from nltk.corpus import stopwords

from . import text_cleaner
from . import text_tokenizer
from . import data_moulder
from . import invoke_training_data
from . import save_and_load_classifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split


gr_headers = ['Features', 'Vectorizer', 'Classifier', 'False Neg', 'False Pos', 'F1']


####################################
# Generates pipeline classifier. ###
####################################
def bwc_mnnb():
    '''
    bwc: Bag of Words Counts
    mnnb: Multinomial Naive Bayes

    bwc_mnnb(): creates a pipeline with a vectorizer (CountVectorizer()) and a classifier (MultinomialNB())

    :return: list = [a, b, c], where:
             a: type of features that this vectorizer transform the words
             b: name of the vectorizer
             c: name of the classifier
    '''

    pipeline = Pipeline([
        ('count_vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    pipe_info = ["Bag of Words counts", "CountVectorizer", "MultinomialNB", pipeline]

    return pipe_info


######################################################
# Create and train a classifier inside a pipeline. ###
######################################################
def create_pipeline_classifier():
    invocation = invoke_training_data.invoke_data()

    data = invocation[0]
    text_column = invocation[1]
    class_column = invocation[2]

    print(data.head())

    clf = bwc_mnnb()
    classifier_infos = dict()
    scores = []
    confusion = np.array([[0, 0], [0, 0]])

    k_fold = KFold(n=len(data), n_folds=10)

    for train_indices, test_indices in k_fold:
        # Gathering Train folds.
        train_text = data.iloc[train_indices][text_column].values
        train_y = data.iloc[train_indices][class_column].values

        # Gathering Test folds
        test_text = data.iloc[test_indices][text_column].values
        test_y = data.iloc[test_indices][class_column].values

        clf[3].fit(train_text, train_y)
        predictions = clf[3].predict(test_text)

        confusion += confusion_matrix(test_y, predictions)

        score = f1_score(test_y, predictions, pos_label=0)
        scores.append(score)

        update_classifier_results(classifier_infos, clf, confusion, scores)

    print_classifier_infos(classifier_infos)
    save_and_load_classifier.save_classifier(clf[3], 'multinomialNB')
    print('SAVED')

    #return clf[3]


#######################################
####### NAIVE BAYES prediction ########
#######################################
def classify_sentence(sentence, classifier):
    # Without negation handling.
    list_sentence = []
    list_sentence.append(sentence)

    # With negation handling.
    #sentence_negative = data_moulder.negate_sentence(sentence)
    #list_sentence.append(sentence_negative)

    # Convert string into numpy array.
    input_text = np.array(list_sentence)

    # Classify sentence.
    clf_value = classifier.predict(input_text)
    #print("Classification result: " + str(clf_value))

    return clf_value


##################################################################
# Split document, classify the sentence and summarize aspects. ###
##################################################################
def sentiment_summarization(summary_dict, sentiment_polarity):
    if sentiment_polarity[0] > 0:
        summary_dict['Score'][0] += 1
    else:
        summary_dict['Score'][1] += 1


###########################################################
# Predict text sentiment and update aspects dictionary. ###
###########################################################
def predict_text(text, summary_dict, classifier):
    # Cleaning text.
    clean_text = text_cleaner.text_cleansing(text)

    sentiment_polarity = classify_sentence(clean_text, classifier)
    sentiment_summarization(summary_dict, sentiment_polarity)

    # Slipt input text into sentences.
    #text_sentences = text_tokenizer.split_in_sentences(clean_text)

    #for sentence in text_sentences:
    #    sentiment_polarity = classify_sentence(sentence, classifier)
    #    sentiment_summarization(summary_dict, sentiment_polarity)


##################################################
# Update the classifier's informations values. ###
##################################################
def update_classifier_results(classifier_infos, pipe_info, confusion, f1_scores):
    classifier_infos[gr_headers[0]] = pipe_info[0]
    classifier_infos[gr_headers[1]] = pipe_info[1]
    classifier_infos[gr_headers[2]] = pipe_info[2]
    classifier_infos[gr_headers[3]] = confusion[0, 1]
    classifier_infos[gr_headers[4]] = confusion[1, 0]
    classifier_infos[gr_headers[5]] = sum(f1_scores) / len(f1_scores)


####################################
# Print classifier informations. ###
####################################
def print_classifier_infos(classifier_infos):
    print("Features: " + classifier_infos[gr_headers[0]])
    print("Vectorizer: " + classifier_infos[gr_headers[1]])
    print("Classifier: " + classifier_infos[gr_headers[2]])
    print("False Neg: " + str(classifier_infos[gr_headers[3]]))
    print("False Pos: " + str(classifier_infos[gr_headers[4]]))
    print("F1 Score: " + str(classifier_infos[gr_headers[5]]))
