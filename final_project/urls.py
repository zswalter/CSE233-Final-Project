from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.contrib import admin
from cse233care import views

urlpatterns = patterns('',
    url('^$', views.main_view, name='index'),
    url('^logged_in$', views.logged_in_view, name='logged_in'),
    url('^register1$', views.register1, name='register1'),
    url('^register2$', views.register2, name='register2'),
    url('^register3$', views.register3, name='register3'),
)
