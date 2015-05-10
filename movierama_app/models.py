from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html

class Movie(models.Model):
    # relations
    creator = models.ForeignKey(User)
    liked_by = models.ManyToManyField(User, through='Action', related_name='likers')
    #properties
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def likes(self):
        return self.action_set.all().filter(action=LIKE).count()
    def hates(self):
        return self.action_set.all().filter(action=HATE).count()
    def get_user_comments(self):
        movie_comment = self.action_set.all()
        # return self.action_set.all()
        return {
            'likes': movie_comment.filter(action=LIKE).count(),
            'hates': movie_comment.filter(action=HATE).count()
        }
    def get_user_comments_admin(self):
        movie_comment = self.action_set.all()
        return  format_html('<span style="color: red;">Likes: {} and hates {}</span>'.format(movie_comment.filter(action=LIKE).count(), movie_comment.filter(action=HATE).count()))
    def __str__(self):
        return self.title

LIKE = 0
HATE = 1

COMMENT_CHOICES = (
    (LIKE , 'like'),
    (HATE , 'hate')
)

class Action(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    action = models.IntegerField(choices=COMMENT_CHOICES)
    def __str__(self):
        action_verb = self.action == LIKE and 'likes' or 'hates'
        return "{} {} {}".format(self.user, action_verb, self.movie)

