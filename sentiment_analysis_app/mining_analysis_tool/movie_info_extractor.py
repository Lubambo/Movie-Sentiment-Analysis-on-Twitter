import re


# Extract the movie's year from the user input.
def get_movie_year(user_input):
    pattern = r"\(\d+\)"
    year = re.findall(pattern, user_input)[0][1:-1]

    return year


# Extract the movie's title from the user input.
def get_movie_title(user_input):
    pattern = r"^[\w\W\d\D]+\s\("
    title_match = re.findall(pattern, user_input)
    title = title_match[0][:-2]     # Removing end space and parentheses.

    return title
