from django.shortcuts import render
from . import views_classes
from mining_analysis_tool import tool_facade


def index(request):
    html_path = 'portal/home.html'
    return render(request, html_path)


def run_analysis(request):
    html_path = 'portal/run_analysis.html'

    if request.method == 'POST':
        movie_title = request.POST.get('search_bar', None)

        if movie_title is not None:
            sentiment_summary = tool_facade.make_sentiment_dict()

            tweets = tool_facade.tweets_miner(movie_title)
            quantity = 'Quantidade de tweets extraídos: ' + str(len(tweets))

            tool_facade.analyse_tweets(tweets, sentiment_summary)

            movie_score = tool_facade.get_movie_rate(sentiment_summary)
            movie_score_info = "Movie rate: " + movie_score

            sent_percent = tool_facade.get_sentiments_percentages(sentiment_summary)
            sentiment = sent_percent
            #sentiment = "Positivo: " + sent_percent[0] + "%  |  "
            #sentiment += "Negativ0: " + sent_percent[1] + "%"

            number_of_analysis = tool_facade.get_number_of_analysis(sentiment_summary)
            analyzed_qty = "Quantidade de tweets analisados: " + number_of_analysis

            return render(request, html_path, {'tweets': tweets, 'qty': quantity, 'rate': movie_score_info, 'sentiment': sentiment, 'analysis': analyzed_qty})

    else:
        return render(request, html_path)
