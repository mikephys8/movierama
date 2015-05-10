# -*- coding: utf-8 -*-
import json
from datetime import timedelta, datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from movierama_app.forms import UserForm
from movierama_app.models import *
from movierama_app.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# helpers
def movies_parser(m):
    return {
        "movie_id": m.id,
        "title": m.title,
        "description": m.description,
        "actions": m.get_user_comments,
        "pub_date": (datetime.now() - m.pub_date.replace(tzinfo=None)).days,
        "creator": m.creator
    }

def user_action(a):
    return  a.id

def home(request):
    try :
        f =request.GET['username']
    except:
        f = None

    if f:
        movies_data = map(movies_parser, Movie.objects.filter(creator=User.objects.get(username=request.GET['username'])))
    else:
        movies_data = map(movies_parser, Movie.objects.all())

    if request.user.is_authenticated():
        movies_commented = request.user.likers.all()
        user_movies_liked = map(user_action, movies_commented.filter(action__action=0))
        user_movies_hated = map(user_action, movies_commented.filter(action__action=1))
        for m in movies_data:
            if m['movie_id'] in user_movies_liked:
                m['action_value'] = 0
            elif m['movie_id'] in user_movies_hated:
                m['action_value'] = 1
            else:
                m['action_value'] = None
        data = {
            "complete_user": request.user,
            "movies": movies_data,
            }
    else:
        data = {
            "complete_user":  request.user,
            "movies": movies_data
        }
    return render(request, 'home.html', data )

def user_login(request):
    usr = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('login_fail.html', usr)
    else:
        return render_to_response('login.html', {}, usr)

@csrf_exempt
def register(request):
    reg = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('register.html',
                              {'user_form': user_form, 'registered': registered},
                              reg)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def create_movie(request):
    if request.method == 'POST':
        form = NewMovie(request.POST)
        if form.is_valid():
            movie = form.save(commit = False)
            movie.creator = request.user
            movie.pub_date = models.DateTimeField(auto_now=True)
            movie.save()
            return HttpResponseRedirect('/')
    else:
        form = NewMovie()
    return render(request, 'create_movie.html', {'form': form, })

def action(request, movie_id, action_id):
    action_value = int(action_id)
    movie = Movie.objects.get(id=movie_id)
    existing_action, created = Action.objects.get_or_create(user=request.user,
                                                            movie=movie,
                                                            defaults={'action': action_value})
    if not created:
        existing_action.action = action_value
    #     dev stuff
    act = action_value == 0 and 'likes' or 'hates'
    return HttpResponse(json.dumps({
        "message": request.user.username + " {} ".format(act) + movie.title
    }))

def action_delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    act = Action.objects.get(user=request.user,movie=movie)
    act.delete()
    return HttpResponse(json.dumps({
        "message": 'deleted'
    }))