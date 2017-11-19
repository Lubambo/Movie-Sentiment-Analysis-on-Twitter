import re

###################################
######### Text Treatment ##########
###################################
######################
# Remove e-mail's. ###
######################
def remove_emails(text):
    regex = r"[^@\s]*@[^@\s]*\.[^@\s]*"

    clean_text = re.sub(regex, "usermail", text)
    # print(clean_text)

    return clean_text


###################
# Remove uri's. ###
###################
def remove_urls(text):
    regex = r"(www?\S+)|(https?://)([\w\.]+[\w])+(:\d+)?(/([\w/_\.#-]*(\?\S+)?[^\.\s])?)?"

    clean_text = re.sub(regex, "urltext", text)
    # print(clean_text)

    return clean_text


##############################################
# Separete word from previous punctuation. ###
##############################################
def remove_previous_punctuation(text):
    regex = r"[\.\\/]\w+"
    matches = re.finditer(regex, text)

    clean_text = text
    # print(clean_text)

    for match in matches:
        replacement = ''

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            match_group = match.group(groupNum)

            if groupNum < len(match.groups()):
                replacement += match_group + " "
            else:
                replacement += match_group

                # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        # print(replacement)

        clean_text = clean_text.replace(match.group(), replacement)
        # print(clean_text)

    return clean_text


################################################################
# Connect back hyphenated words, splitted by text cleansing. ###
################################################################
def connect_hyphenation(text):
    regex = r"\w+-\s\w+"
    matches = re.finditer(regex, text)

    clean_text = text
    # print(clean_text)

    for match in matches:
        replacement = ''

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            match_group = match.group(groupNum)

            replacement += match_group

            # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        # print(replacement)

        clean_text = clean_text.replace(match.group(), replacement)
        # print(clean_text)

    return clean_text


###############################################
# Remove \ between pronome and abreviation. ###
# Like so: it\' and 25\' ######################
###############################################
def remove_pronomes_backslash(text):
    regex = r"(\\)(')"
    matches = re.finditer(regex, text)

    clean_text = text
    # print(clean_text)

    for match in matches:
        replacement = ''

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            match_group = match.group(groupNum)

            if match_group == '\\':
                replacement += ''
            else:
                replacement += match_group

                # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        # print(replacement)

        clean_text = clean_text.replace(match.group(), replacement)
        # print(clean_text)

    return clean_text


#############################################################
# Separates words from punctuation. Also removes \ and /. ###
#############################################################
def disconnect_word_from_punctuation(text):
    # words: (\w+)
    # all punctuations: ([.,\/#!$%\^&\*;:{}=\-_`~()])
    regex = r"(\w+)([.,\/#!$%\^&\*;:{}=\-_`~()]+)([A-Za-z0-9])"

    matches = re.finditer(regex, text)

    clean_text = text
    # print(clean_text)

    ignore_replacement = ['\\', '/', '*']

    for match in matches:
        replacement = ''

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            match_group = match.group(groupNum)

            # if match_group == '\\' or match_group == '/':
            if match_group in ignore_replacement:
                replacement += ''
            else:
                if groupNum < len(match.groups()):
                    replacement += match_group + " "
                else:
                    replacement += match_group

                    # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        # replacement += " "
        # print(replacement)

        clean_text = clean_text.replace(match.group(), replacement)
        # print(clean_text)

    return clean_text


##############################
# Remove excessive spaces. ###
##############################
def remove_excessive_spaces(text):
    # Remove excessive middle spaces.
    regex = r"\s+"
    no_exc_spc_text = re.sub(regex, " ", text)

    # Remove excessive end spaces.
    regex = r"\s$"
    clean_text = re.sub(regex, "", no_exc_spc_text)

    return clean_text


###################################
# Remove data extracion noises. ###
###################################
def remove_extraction_noise(text):
    regex = r"^b"
    no_b = re.sub(regex, "", text)

    regex = r"^'"
    no_start_apostrophe = re.sub(regex, "", no_b)

    regex = r"'$"
    no_end_apostrophe = re.sub(regex, "", no_start_apostrophe)

    return no_end_apostrophe


#####################
# Text cleansing. ###
#####################
def text_cleansing(text):
    no_email_text = remove_emails(text)
    no_urls_text = remove_urls(no_email_text)
    fixed_wp_text = disconnect_word_from_punctuation(no_urls_text)
    fixed_spaces_text = remove_excessive_spaces(fixed_wp_text)
    no_prev_punc_text = remove_previous_punctuation(fixed_spaces_text)
    clean_text = connect_hyphenation(no_prev_punc_text)

    return clean_text
