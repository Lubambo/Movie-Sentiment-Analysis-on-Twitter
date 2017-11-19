import tweepy
import unicodedata
import html
from . import text_cleaner


consumer_key = 'L9D22X5EVZRP6FowS4tjq2ruI'
consumer_secret = 'keeXNoGEQsvmjzTgbeBxu0kEN2nxPzAI5K9DqGI04buBAFySsf'

access_token = '902905428681613316-XIE5hG6kb6JqQ6MDkVwJXdlQzfSzz0s'
access_token_secret = 'HamzCI2sKuBGyIpvg89azwOfptPsoCFCdqO3GBeQQYQyt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)


###################################
# Save tweets into a .txt file. ###
###################################
def tweets_to_txt(tweets_list, file_name):
    not_allowed = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|']
    name = ''

    for character in file_name:
        if character not in not_allowed:
            name += name.join(character)

    file_path = r'C:\Users\Felipe\Documents\Programação\ADS\4º Período\\' + name + ".txt"
    with open(file_path, 'w+') as file:
        for tweet in tweets_list:
            html_tweet_scape = html.unescape(tweet)
            treated_tweet = unicodedata.normalize('NFKD', html_tweet_scape).encode('ascii', 'ignore')
            tweet_str = str(treated_tweet)
            clean_tweet = text_cleaner.remove_extraction_noise(tweet_str)
            file.write("%s\n" % clean_tweet)


#######################################################
# Appends to the tweets list only tweets withou RT. ###
#######################################################
def get_tweet_without_RT(tweets_request, tweets_list_to_append):
    tweet_id = -1
    for tweet in tweets_request:
        tweet_id = tweet.id
        if tweet.retweet_count == 0:
            tweets_list_to_append.append(tweet.full_text)

    return tweet_id


#######################################################
# Appends to the tweets list only tweets withou RT. ###
#######################################################
def get_tweet_with_RT(tweets_request, tweets_list_to_append):
    tweet_id = -1
    for tweet in tweets_request:
        tweet_id = tweet.id
        tweets_list_to_append.append(tweet.full_text)

    return tweet_id


##############################################
# Mine Twitter looking for the movie_name. ###
##############################################
def mine_twitter(movie_name, exclude_RT=False):
    tweets_count = 500
    request_tweets_count = 100

    query = "\"" + movie_name + "\"" + " movie OR watch OR watched OR go OR gone OR see OR saw OR must OR should OR recommend OR rated OR rate -trailer -trailers -online -download -clip -clips -@YouTube"
    timeline_first_request = twitter_api.search(q=query, lang='en', count=request_tweets_count, tweet_mode='extended')

    tweet_id = 0
    tweets_text = []

    if exclude_RT:
        last_id = get_tweet_without_RT(timeline_first_request, tweets_text) - 1

        for count in range(request_tweets_count, tweets_count, request_tweets_count):
            timeline = twitter_api.search(q=query, lang='en', count=request_tweets_count, max_id=last_id, tweet_mode='extended')
            last_id = get_tweet_without_RT(timeline, tweets_text) - 1
    else:
        last_id = get_tweet_with_RT(timeline_first_request, tweets_text) - 1

        for count in range(request_tweets_count, tweets_count, request_tweets_count):
            timeline = twitter_api.search(q=query, lang='en', count=request_tweets_count, max_id=last_id,
                                          tweet_mode='extended')
            last_id = get_tweet_with_RT(timeline, tweets_text) - 1

    #for text in tweets_text:
    #    print(text)
    #    print()
    tweets_to_txt(tweets_text, movie_name)
    #print("Número de tweets extraídos do usuário: " + str(len(tweets_text)))
    return tweets_text
