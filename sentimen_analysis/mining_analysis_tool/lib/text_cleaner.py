import re


# Remove e-mail's.
def remove_emails(text):
    regex = r"[^@\s]*@[^@\s]*\.[^@\s]*"

    clean_text = re.sub(regex, "usermail", text)

    return clean_text


# Remove uri's.
def remove_urls(text):
    regex = r"(www?\S+)|(https?://)([\w\.]+[\w])+(:\d+)?(/([\w/_\.#-]*(\?\S+)?[^\.\s])?)?"

    clean_text = re.sub(regex, "urltext", text)

    return clean_text


# Remove excessive spaces.
def remove_excessive_spaces(text):
    # Remove excessive middle spaces.
    regex = r"\s+"
    no_exc_spc_text = re.sub(regex, " ", text)

    # Remove excessive end spaces.
    regex = r"\s$"
    clean_text = re.sub(regex, "", no_exc_spc_text)

    return clean_text


# Remove data extracion noises.
def remove_extraction_noise(text):
    regex = r"^b"
    no_b = re.sub(regex, "", text)

    regex = r"^'"
    no_start_apostrophe = re.sub(regex, "", no_b)

    regex = r"'$"
    no_end_apostrophe = re.sub(regex, "", no_start_apostrophe)

    return no_end_apostrophe


# Remove '#' from hashtags, leaving only words.
def remove_hashtag(text):
    regex = r"#([A-Za-z0-9])*"
    matches = re.finditer(regex, text)

    clean_text = text

    for match in matches:
        replacement = ''

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            match_group = match.group(groupNum)

            if match_group == '#':
                replacement += ' '
            else:
                replacement += match_group

        clean_text = clean_text.replace(match.group(), replacement)

    return clean_text


# Text cleansing.
def text_cleansing(text):
    no_email_text = remove_emails(text)
    no_urls_text = remove_urls(no_email_text)
    fixed_spaces_text = remove_excessive_spaces(no_urls_text)
    clean_text = remove_hashtag(fixed_spaces_text)

    return clean_text
