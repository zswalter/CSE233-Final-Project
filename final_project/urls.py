from django.conf.urls import patterns, include, url

# from django.contrib import admin
from cse233care import views

urlpatterns = patterns('',
    url('^$', views.mainview, name='index'),
)
