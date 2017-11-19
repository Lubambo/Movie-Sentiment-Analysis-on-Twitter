import numpy as np

import matplotlib.pyplot as plt

from . import translate_info


def get_summary_dict_key(summary_dict):
    score_key = ''
    for key in summary_dict:
        score_key = key

    return score_key

#####################################
# Show sentiment polarity scores. ###
#####################################
def summarize_sent_polarity_scores(results_dict):
    sent_pol_val = list(results_dict.values())

    pos = 0
    neg = 0
    for i in range(len(sent_pol_val)):
        pos += sent_pol_val[i][0]
        neg += sent_pol_val[i][1]

    #print("POS: " + str(pos))
    #print("NEG: " + str(neg))

    scores = {
        "Score": [pos, neg]
    }

    return scores


#
#
#
def save_plot_image(file_name):
    save_directory = 'graph_images/'
    file_extension = '.png'
    save_path = save_directory + file_name + file_extension
    plt.savefig(save_path)


#################
# Draw graph. ###
#################
def draw_plot(left_bar_values, right_bar_values, bar_groups_number, plot_title='', x_axis_label='', y_axis_label='',
              bar_groups_labels=[], legend_left_bar='', legend_right_bar='', insert_legend=True):

    # Create plot.
    plt.subplot()

    # Plot bars dimmensions.
    n_groups = bar_groups_number
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 1

    # Create the left bar, for positive value
    plt.bar(index, left_bar_values, bar_width,
            alpha=opacity,
            color='#283593',
            label=legend_left_bar)

    # Create the right bar, for negative value
    plt.bar(index + bar_width, right_bar_values, bar_width,
            alpha=opacity,
            color='#C62828',
            label=legend_right_bar)

    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(plot_title)
    plt.xticks(index + bar_width, bar_groups_labels)

    if insert_legend:
        plt.legend()

    plt.tight_layout()


#######################
# Plotting summary. ###
#######################
def plot_summary(results_dict, movie_name='Nome do Filme'):
    pos_value = []
    neg_value = []
    x_axis_names = []

    for key in results_dict:
        x_axis_names.append(key)
        pos_value.append(results_dict[key][0])
        neg_value.append(results_dict[key][1])

    x_axis_translated_names = translate_info.translate_words(x_axis_names)

    number_of_groups = len(results_dict)
    draw_plot(pos_value, neg_value, number_of_groups, plot_title=movie_name, x_axis_label='',
              y_axis_label='Número de comentários', bar_groups_labels=x_axis_translated_names,
              legend_left_bar='Positivo', legend_right_bar='Negativo')

    save_plot_image('aspects_summary')
    plt.show()
    # Clear plot.
    # plt.clf()


######################################
# Plot sentiment polarity summary. ###
######################################
def plot_polarity_scores(scores_dict, movie_name='Nome do Filme'):
    score_key = get_summary_dict_key(scores_dict)

    pos_value = []
    neg_value = []

    pos_value.append(scores_dict[score_key][0])
    neg_value.append(scores_dict[score_key][1])

    number_of_groups = len(scores_dict)
    draw_plot(pos_value, neg_value, number_of_groups, plot_title=movie_name, x_axis_label='',
              y_axis_label='Número de comentários', legend_left_bar='Positivo', legend_right_bar='Negativo')

    save_plot_image('sentiment_polarity')
    plt.show()
    # Clear plot.
    # plt.clf()


#####################################
# Show sentiment polarity scores. ###
#####################################
def sent_polarity_scores(results_dict, movie_name='Nome do Filme'):
    #scores = summarize_sent_polarity_scores(results_dict)
    plot_polarity_scores(results_dict, movie_name)


#########################################
# Calculate percantage of each score. ###
#########################################
def score_percentage(results_dict):
    score_key = get_summary_dict_key(results_dict)

    total_scores = results_dict[score_key][0] + results_dict[score_key][1]

    if total_scores > 0:
        positive_percent = (results_dict[score_key][0] / total_scores) * 100
        negative_percent = (results_dict[score_key][1] / total_scores) * 100
        percents = [positive_percent, negative_percent]
    else:
        percents = [0, 0]

    return percents


#########################
# Informs movie rate. ###
#########################
def movie_rate(results_dict):
    #scores = summarize_sent_polarity_scores(results_dict)
    score_key = get_summary_dict_key(results_dict)

    total_scores = results_dict[score_key][0] + results_dict[score_key][1]
    negative_scores = results_dict[score_key][1]

    movie_score = 0

    if total_scores > 0:
        movie_score = ( ( total_scores - negative_scores ) / total_scores ) * 10

    return movie_score


##########################################
# Verify how many texts were analysed. ###
##########################################
def texts_analysed(results_dict):
    counter = 0

    for key in results_dict:
        counter += results_dict[key][0]
        counter += results_dict[key][1]

    return counter
