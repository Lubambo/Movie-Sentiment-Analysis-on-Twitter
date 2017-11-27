from cassandra.cluster import Cluster
import string


# Get the movie's information on database.
def get_movie_status(movie_title, movie_year):

    """
    Queries the database for all the movie's information;

    :param
    movie_title: movie's title;
    movie_year: movie's year;

    :return:
    return a dictionary list with the query's result
        |-> the dictionary is like:
            {
            'title': ,
            'year': ,
            'plot': ,
            'image': ,
            'positive': ,
            'negative': ,
            'last_id':
            }
            where:
                |-> title: movie's title;
                |-> year: movie's year;
                |-> plot: movie's plot;
                |-> image: movie's image,
                |-> positive: number of positive tweets;
                |-> negative: number of negative tweets;
                |-> last_id: id of the most recent extracted tweet.
    """

    try:
        cluster = Cluster()
        session = cluster.connect('movie_db')

        try:
            # Query the movie's rates.
            query = """select title, year, plot, image, positive_rate, negative_rate, last_id from movie
                            where title = %(title)s
                            and year = %(year)s"""
            param = {
                'title': movie_title,
                'year': movie_year
            }

            row = session.execute(query, param)

            title = ''
            year = ''
            plot = ''
            image = ''
            positive = 0
            negative = 0
            last_id = ''

            try:
                for r in row:
                    title = r.title
                    year = r.year
                    plot = r.plot
                    image = r.image
                    positive = r.positive_rate
                    negative = r.negative_rate
                    last_id = r.last_id

                if title is None:
                    title = ''
                if year is None:
                    year = ''
                if plot is None:
                    plot = ''
                if image is None:
                    image = ''
                if positive is None:
                    positive = 0
                if negative is None:
                    negative = 0
                if last_id is None:
                    last_id = ''

                results = {
                    'title': title,
                    'year': year,
                    'plot': plot,
                    'image': image,
                    'positive': positive,
                    'negative': negative,
                    'last_id': last_id
                }
            except:
                results = {
                    'title': '',
                    'year': '',
                    'plot': '',
                    'image': '',
                    'positive': 0,
                    'negative': 0,
                    'last_id': ''
                }

            return results

        except:
            print("UNSUCCESSFUL QUERY!")
            return {'title': '', 'year': '', 'plot': '', 'image': '', 'positive': 0, 'negative': 0, 'last_id': ''}

    except:
        print("NO DATABASE CONNECTION!")
        return {'title': '', 'year': '', 'plot': '', 'image': '', 'positive': 0, 'negative': 0, 'last_id': ''}


# Get movies title and launch year.
def get_autocomplete_movie_title(parcial_title):

    """
    Used to query the database for movies that contain 'parcial_title' in the title;

    :param:
    parcial_title: parcial name of the movie's title;

    :return:
    return a dictionary list with the query's result
        |-> the dictionary is like:
            {
            'title': '',
            'year': ,
            }
            where:
                |-> title is the movie's title;
                |-> year is the movie's launch year;
    """

    try:
        cluster = Cluster()
        session = cluster.connect('movie_db')

        try:
            if len(parcial_title) < 2:
                # Query all movies that the title start with parcial_title, as it is just on letter.
                query = """select title, year from movie_autocomplete
                                where first_letter = %(first_letter)s
                                and title >= %(parcial_title)s"""
                param = {
                    'first_letter': parcial_title[0],
                    'parcial_title': parcial_title
                }
            else:
                # Query all movies with range for autocomplete.
                query = """select title, year from movie_autocomplete
                                where first_letter = %(first_letter)s
                                and title >= %(parcial_title)s
                                and title < %(top_limit)s"""

                if parcial_title[-1] == 'z' or parcial_title[-1] == 'Z':
                    # If the last character is z or Z, nothing changes.
                    top_limit = parcial_title
                else:
                    # Change the last character of the parcial_title to it's successor.
                    top_limit = parcial_title[0:-1] + chr(ord(parcial_title[-1]) + 1)

                param = {
                    'first_letter': parcial_title[0],
                    'parcial_title': parcial_title,
                    'top_limit': top_limit
                }

            rows = session.execute(query, param)

            results = {'movies': []}

            for row in rows:
                result = {
                    'title': string.capwords(row.title),
                    'year': row.year
                }
                results['movies'].append(result)

            return results

        except:
            print("UNSUCCESSFUL QUERY!")
            return {'movies': []}

    except:
        print("NO DATABASE CONNECTION!")
        return {'movies': []}


# Update the number of tweets of each sentiment (positive and negative).
def update_movie_status(movie_title, movie_year, positive_value, negative_value, last_id):

    """
    Queries the database for movie's last id and tweets quantity, then update their values;

    :param
    movie_title: movie's title;
    movie_year: movie's year;
    positive_value: value to update positive_rate of the movie;
    negative_value: value to update negative_rate of the movie;
    last_id: value to update last id of the most recent extraced tweet;

    :return:
    """

    try:
        cluster = Cluster()
        session = cluster.connect('movie_db')

        try:
            # Query to update movie's rates and last_id.
            query = """update movie
                            set positive_rate = %(positive)s, negative_rate = %(negative)s, last_id = %(last_id)s
                            where title = %(title)s
                            and year = %(year)s"""

            param = {
                'title': movie_title,
                'year': movie_year,
                'positive': positive_value,
                'negative': negative_value,
                'last_id': str(last_id)
            }

            session.execute(query, param)

        except:
            print("UNSUCCESSFUL QUERY!")

    except:
        print("NO DATABASE CONNECTION!")
