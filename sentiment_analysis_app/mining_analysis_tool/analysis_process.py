import math

from mining_analysis_tool import database_access
from mining_analysis_tool import lib_facade


# Analysis process
def run_analysis(movie_title, movie_year):
    """
    Works as a facade to the process of analysis of the given movie's title and year.
    It has three stages:
        1. Get the given movie data on database;
        2. Call Twitter miner and analyse the tweets, getting the analysis' data from it.
        3. Update the values of movie status.

    :param movie_title: movie's title;
    :param movie_year: movie's year;
    :return: summarized data as a dict.
    """
    # Get database tweets quantity of that movie.
    database_data = database_access.get_movie_status(movie_title, movie_year)
    # Database most recent tweet id.
    database_last_id = database_data['last_id']

    # Get that movie's analysis data.
    try:
        analysis_data = lib_facade.get_analysis_data(movie_title, int(database_last_id))
    except (TypeError, ValueError):
        analysis_data = lib_facade.get_analysis_data(movie_title)

    # Most recent extracted tweet id.
    analysis_last_id = str(analysis_data['last_id'])

    database_total = database_data['positive'] + database_data['negative']
    analysis_total = analysis_data['tweets_qty']

    # Total of tweets analyised so far.
    general_total = database_total + analysis_total

    # Positive score.
    positive_total = database_data['positive'] + analysis_data['positive']
    positive_rate = positive_total / general_total
    positive = math.floor(positive_rate * 100) / 100

    # Negative score.
    negative_total = database_data['negative'] + analysis_data['negative']
    negative_rate = negative_total / general_total
    negative = math.floor(negative_rate * 100) / 100

    # Movie's rate.
    rate = math.floor((positive * 10) * 100) / 100

    # Check if the most recent id on database is the same of the analysis.
    # If it is, nothing new has come from this analysis.
    if database_last_id == analysis_last_id:
        same_id = True
    else:
        same_id = False

    # If the ids are equal, the database does not change.
    if same_id:
        data = {
            'title': database_data['title'],
            'year': database_data['year'],
            'plot': database_data['plot'],
            'image': database_data['image'],
            'tweets': analysis_data['tweets'],
            'sentiment': [positive, negative],
            'rate': rate,
            'analysis': general_total
        }
        return data

    else:
        # Update movie's last_id, positive and negative values in the database.
        database_access.update_movie_status(movie_title, movie_year, positive_total, negative_total,
                                            analysis_last_id)

        data = {
            'title': movie_title,
            'year': movie_year,
            'plot': '',
            'image': '',
            'tweets': analysis_data['tweets'],
            'sentiment': [positive, negative],
            'rate': rate,
            'analysis': general_total
        }
        return data
