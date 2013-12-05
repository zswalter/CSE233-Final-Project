from django.conf.urls import patterns, include, url

# from django.contrib import admin
from cse233care import views

urlpatterns = patterns('',
    url('^$', views.main_view, name='index'),
    url('^logged_in$', views.logged_in_view),
    url('^register$', views.register),
)
