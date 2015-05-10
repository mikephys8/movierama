from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie_rama import settings

urlpatterns = patterns('',
    url(r'^$', 'movierama_app.views.home', name='home'),
    url(r'^movierama_app/', include('movierama_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),

)
