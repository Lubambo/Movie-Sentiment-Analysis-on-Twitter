import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


######################################
######### Text tokenization ##########
######################################
#############################################
# Split the text document into sentences. ###
#############################################
def split_in_sentences(text_document):
    '''
    Split the document in sentences.
    '''
    sentences = sent_tokenize(text_document)
    # print(sentences)
    return sentences


####################################
# Split the sentence into words. ###
####################################
def split_in_words(sentence):
    '''
    Split the sentence in words.
    '''
    words = word_tokenize(sentence)
    return words


########################
# Tokenize sentence. ###
########################
def tokenize_sentence(sentence):
    '''
    Tokenize the sentence words in unigrams.
    input:
        - sentence: string the will be tokenized;
    output:
        - return an array of tokenized words;
    '''

    # Tokenize only words, ignoring punctuation
    tokenizer = RegexpTokenizer(r'\w+')

    return tokenizer.tokenize(sentence)


############################
# Tokenize data's texts. ###
############################
def tokenize_data_texts(data, text_column):
    rows = data.shape[0]

    for row in range(rows):
        text = data.loc[row, text_column]

        tokenized_text = tokenize_sentence(text)

        data.set_value(row, text_column, tokenized_text)


####################
# POS tag words. ###
####################
def pos_tag_words(words_array):
    '''
    POS tag the words in the 'words_array'.
    '''
    return nltk.pos_tag(words_array)


###########################
# POS tag the document. ###
###########################
def pos_tag_sentence(text_document):
    '''
    Split the document in sentences, then in words. After that, all words are POS tagged.
    The function returns a list of words pos tagged.
    '''

    sentences = split_in_sentences(text_document)
    # print(sentences)
    tags = []
    try:
        for s in sentences:
            words = split_in_words(s)
            tags.append(pos_tag_words(words))
    except:
        print('error!')

    # print(tags)
    return tags


##########################################
# Tokenize sentence words in unigrams. ###
##########################################
def tokenize_sentence_in_unigram(sentence):
    '''
    Tokenize the sentence words in unigrams.
    input:
        - sentence: string the will be tokenized;
    output:
        - return an array of tokenized words;
    '''
    # Tokenize only words, ignoring punctuation
    tokenizer = RegexpTokenizer(r'\w+')

    return tokenizer.tokenize(sentence)
