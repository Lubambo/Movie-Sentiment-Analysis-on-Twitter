from django.shortcuts import render
from mining_analysis_tool import analysis_process, database_access, movie_info_extractor

import json

from django.http import Http404, HttpResponse


def index(request):
    html_path = 'portal/home.html'
    return render(request, html_path)


def run_analysis(request):
    html_path = 'portal/run_analysis.html'

    if request.method == 'POST':
        user_input = request.POST.get('search_bar', None)

        movie_title = movie_info_extractor.get_movie_title(user_input).lower()
        movie_year = movie_info_extractor.get_movie_year(user_input)

        if (movie_title is not None) and (movie_year is not None):
            data = analysis_process.run_analysis(movie_title, movie_year)

            return render(request, html_path, data)

    else:
        return render(request, html_path)


def autocomplete_ajax(request):
    if request.is_ajax():
        movie_title = request.GET['movie_title']

        movies = database_access.get_autocomplete_movie_title(movie_title)

        data = json.dumps(movies)

        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
