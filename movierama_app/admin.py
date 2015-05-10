from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.utils.html import format_html
from movierama_app.models import Movie, Action

def getLikes(self):
    return format_html('<span>{}</span>'.format(self.action_set.filter(action=0).count()))

def getHates(self):
    return format_html('<span>{}</span>'.format(self.action_set.filter(action=1).count()))

def liked_movies(self):
    html= '<ul>'
    for i in self.likers.filter(action__action=0):
        html = html + '<li>{}</li>'.format(str(i))
    return format_html(html)

def hated_movies(self):
    html= '<ul>'
    for i in self.likers.filter(action__action=1):
        html = html + '<li>{}</li>'.format(str(i))
    return format_html(html)

class MyUserAdmin(admin.ModelAdmin):
    fields = ('username','email', 'password', liked_movies, hated_movies)
    readonly_fields = (liked_movies, hated_movies,)
    list_display = ('username', 'email', getLikes, getHates)

class MovieAdmin(admin.ModelAdmin):

    fields = ('creator', 'title',  'description','pub_date', 'get_user_comments_admin')
    readonly_fields = ('pub_date', 'get_user_comments_admin',)
    list_display = ('title', 'get_user_comments_admin')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Action)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)