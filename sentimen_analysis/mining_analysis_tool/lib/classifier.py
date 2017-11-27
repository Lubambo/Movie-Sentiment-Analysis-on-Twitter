import numpy as np

from . import text_cleaner


# Bayesian classifier.
def classify_sentence(sentence, classifier):
    list_sentence = []
    list_sentence.append(sentence)

    # Convert string into numpy array.
    input_text = np.array(list_sentence)

    # Classify sentence.
    clf_value = classifier.predict(input_text)

    return clf_value


# Split document, classify the sentence and summarize aspects.
def sentiment_summarization(summary_dict, sentiment_polarity):
    if sentiment_polarity[0] > 0:
        summary_dict['Score'][0] += 1   # Positive.
    else:
        summary_dict['Score'][1] += 1   # Negative.


# Predict text sentiment and update aspects dictionary.
def predict_text(text, summary_dict, classifier):
    # Cleaning text.
    clean_text = text_cleaner.text_cleansing(text)

    sentiment_polarity = classify_sentence(clean_text, classifier)
    sentiment_summarization(summary_dict, sentiment_polarity)
