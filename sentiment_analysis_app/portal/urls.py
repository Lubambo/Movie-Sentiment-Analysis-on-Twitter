from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^run_analysis/$', views.run_analysis, name='run_analysis'),
    url(r'^auto_complete/$', views.autocomplete_ajax, name='autocomplete_ajax')
]
