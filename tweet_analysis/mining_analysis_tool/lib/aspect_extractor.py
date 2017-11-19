from nltk.tokenize import word_tokenize
from nltk.corpus   import stopwords

from . import text_tokenizer


#################################################
# Create sentiment polarity score dictionary. ###
#################################################
def create_sentiment_dictionary():
    pos = 0
    neg = 0

    scores = {
        "Score": [pos, neg]
    }

    return scores


######################################
# Create aspects score dictionary. ###
######################################
def create_aspect_dictionary(aspects_set):
    # Preallocate aspects summary dictionary.
    # key: aspect
    # value: array[a, b] of class values, where 'a' is 'positive' and 'b' is 'negative'.
    aspects_summary_dict = dict()

    for word in aspects_set:
        aspects_summary_dict[word] = [0, 0]

    return aspects_summary_dict


#########################
# Aspects extraction. ###
#########################
def get_aspects(tagged_text):
    '''
    The function extracts all aspects of the sentence, by selecting the 'NN' tagged words.
    The return is a set of aspects.
    '''

    aspects_set = set()
    for sentence in tagged_text:
        for aspect in sentence:
            if aspect[1] == 'NN':
                aspects_set.add(aspect[0])

    # print(aspects_set)
    return aspects_set


################################################
# Updating DataFrame's 'text' Series values. ###
################################################
def getting_data_aspects(data, text_column):
    # Raw aspects set.
    aspects_set = set()

    for row in range(data.shape[0]):
        # Get cell's text.
        row_text = data.loc[row, text_column]

        # Edit cell's text.
        # edt_txt = tokenize_sentence_in_unigram(row_text) # This may not be good!!!!
        edt_txt = word_tokenize(row_text)

        tagged_text = text_tokenizer.pos_tag_sentence(row_text)

        # Getting sentence aspects
        for sentence in tagged_text:
            for aspect in sentence:
                if aspect[1] == 'NN':
                    aspects_set.add(aspect[0])

    # Get NLTK stop_words.
    stop_words = set(stopwords.words('english'))

    # Refined aspects set.
    aspects = set()

    # Assembly refined aspects set.
    for word in aspects_set:
        if word not in stop_words:
            aspects.add(word)

    return aspects
