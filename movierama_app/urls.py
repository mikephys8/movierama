from django.conf.urls import patterns, url
from movierama_app import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       # url(r'^/$', RedirectView.as_view(pattern_name='my_named_pattern'),
                       url(r'^accounts/register/', views.register, name='register'),
                       url(r'^accounts/login/', views.user_login, name='login'),
                       url(r'^accounts/logout/', views.user_logout, name='logout'),

                       url(r'^create_movie/', views.create_movie, name='create_movie'),
                       #api urls
                       url(r'^api/action/(?P<movie_id>[0-9]+)/(?P<action_id>[0-1])', views.action, name='action'),
                       url(r'^api/action/delete/(?P<movie_id>[0-9]+)/', views.action_delete, name='action'),
                       )