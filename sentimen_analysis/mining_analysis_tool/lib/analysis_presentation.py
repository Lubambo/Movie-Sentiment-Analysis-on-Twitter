import math


def get_summary_dict_key(summary_dict):
    score_key = ''
    for key in summary_dict:
        score_key = key

    return score_key


# Calculate percantage of each score.
def score_percentage(results_dict):
    score_key = get_summary_dict_key(results_dict)

    total_scores = results_dict[score_key][0] + results_dict[score_key][1]

    if total_scores > 0:
        positive_percent = (results_dict[score_key][0] / total_scores) * 100
        pos_per = math.floor(positive_percent * 100) / 100

        negative_percent = (results_dict[score_key][1] / total_scores) * 100
        neg_per = math.floor(negative_percent * 100) / 100

        percents = [pos_per, neg_per]
    else:
        percents = [0, 0]

    return percents


# Informs movie rate.
def movie_rate(positive_rate):
    return positive_rate * 10
