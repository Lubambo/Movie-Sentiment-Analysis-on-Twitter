from .lib import analysis_presentation
from .lib import aspect_extractor
from .lib import data_analysis
from .lib import twitter_miner
from .lib import counterVect_multinomialNB as cmb


# Creating/training NB Classifier.
#cmb.create_pipeline_classifier()

# Create sentiment summary dictionary.
def make_sentiment_dict():
    return aspect_extractor.create_sentiment_dictionary()


# Twitter miner.
def tweets_miner(movie_name, exclude_rt=False):
    if movie_name is not None:
        return twitter_miner.mine_twitter(movie_name, exclude_rt)
    else:
        print("You need to insert a movie name")


# Analyse the sentiment of all tweets in the file.
def analyse_tweets(tweets, sentiment_summary):
    data_analysis.analyse_data(tweets, sentiment_summary)


# Calculate movie rate.
def get_movie_rate(sentiment_summary):
    film_score = analysis_presentation.movie_rate(sentiment_summary)
    movie_rate = str("%.2f" % film_score)
    return movie_rate


# Printing score percentages.
def get_sentiments_percentages(sentiment_summary):
    scores_percent = analysis_presentation.score_percentage(sentiment_summary)
    #positive = str('%.2f' % scores_percent[0])
    #negative = str('%.2f' % scores_percent[1])
    positive = scores_percent[0]
    negative = scores_percent[1]

    sentiments_percentages = [positive, negative]
    return sentiments_percentages


# Printing number of analysis.
def get_number_of_analysis(sentiment_summary):
    number_of_texts = analysis_presentation.texts_analysed(sentiment_summary)
    analysis = str(number_of_texts)
    return analysis


#movie_title = r'watchmen'
#directory_path = r'C:\Users\Felipe\Documents\Programação\ADS\4º Período\Projeto de sistemas\testes\with_RT_data\\'
#sentiment_summary = make_sentiment_dict()
#tweets_miner(movie_title, exclude_rt=False)
'''
# Testing.
analyse_tweets(movie_title, directory_path)

print("NOTA DO FILME")
movie_score = get_movie_rate(sentiment_summary)
print(movie_score)
print("--------------------")

print("PORCENTAGEM DOS TWEETS")
sent_percent = get_sentiments_percentages(sentiment_summary)
print("Positivo: " + sent_percent[0] + "%")
print("Negativ0: " + sent_percent[1] + "%")
print("--------------------")

print("TEXTOS ANALISADOS")
number_of_analysis = get_number_of_analysis(sentiment_summary)
print("Quantidade: " + number_of_analysis)
'''
