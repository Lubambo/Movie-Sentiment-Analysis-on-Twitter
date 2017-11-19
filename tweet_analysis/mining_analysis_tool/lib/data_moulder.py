#######################################
# Turning score into boolean class. ###
#######################################
def reshape_class(train_data, class_column):
    for i in range(train_data.shape[0]):
        if train_data.loc[i, class_column] > 3.0:
            train_data.loc[i, class_column] = 1    # positive.
        else:
            train_data.loc[i, class_column] = 0    # negative.


################################
# Handling negative on text. ###
################################
def negate_sentence(text):
    '''
    negate_sentence(): negates the text passed on the parameter

    This is used to handle negation words (e.g. not, n't ...).
    Handling negation improves the classification algorithm's accuracy.

    :param text: text to be negated
                |-> type: string
    :return: void
    '''
    negation = False
    delims = "?.,!:;"
    result = []
    words = text.split()

    for word in words:
        stripped = word.strip(delims).lower()
        negated = "not_" + stripped if negation else stripped
        result.append(negated)

        if any(neg in word for neg in ["not", "n't", "no"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    text_result = ' '.join(str(e) for e in result)

    return text_result


#########################
# Data text negation. ###
#########################
def data_text_negation(data, text_column):
    '''
    data_text_negation(): negates all data's texts

    :param data: data to be negated
                |-> type: pandas.DataFrame
    :param text_column: data's text column
                |-> type: string
    :return:void
    '''
    for row in range(data.shape[0]):
        cell_text = data.loc[row, text_column]
        text = negate_sentence(cell_text)

        data.set_value(row, text_column, text)
