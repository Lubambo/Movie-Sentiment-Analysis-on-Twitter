from .lib import sentiment_dictionary_maker
from .lib import data_analysis
from .lib import twitter_miner


# Create sentiment summary dictionary.
def make_sentiment_dict():
    return sentiment_dictionary_maker.create_sentiment_dictionary()


# Twitter miner.
def tweets_miner(movie_name, last_id=0, exclude_rt=False):
    if movie_name is not None:
        return twitter_miner.mine_twitter(movie_name, last_id, exclude_rt)
    else:
        print("You need to insert a movie name")


# Analyse the sentiment of all tweets in the file.
def analyse_tweets(tweets, sentiment_summary):
    data_analysis.analyse_data(tweets, sentiment_summary)


# Group analysis informaiton.
def get_analysis_data(movie_title, last_id=0):
    sentiment_summary = make_sentiment_dict()               # Contains the tweets quantity of each sentiment.

    twitter_minning = tweets_miner(movie_title, last_id)    # Twitter mining.
    tweets = twitter_minning[0]                             # List of tweets extracted.
    new_last_id = twitter_minning[1]                        # ID of the most recent extracted tweet.

    if new_last_id == last_id:
        data = {
            'tweets': tweets,
            'positive': 0,
            'negative': 0,
            'tweets_qty': 0,
            'last_id': new_last_id
        }
    else:
        analyse_tweets(tweets, sentiment_summary)               # Analyse tweets a populate sentiment dict.
        number_of_analysis = sentiment_summary['Score'][0] + sentiment_summary['Score'][1]     # Number of analysed tweets.

        data = {
            'tweets': tweets,
            'positive': sentiment_summary['Score'][0],
            'negative': sentiment_summary['Score'][1],
            'tweets_qty': number_of_analysis,
            'last_id': new_last_id
        }

    return data
