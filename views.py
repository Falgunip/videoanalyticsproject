import hashlib
import json

from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from video_analytics_app.models import analytics_users, video


def showDemoPage(request):
    return render(request,"video_analytics_app/demo.html")


def ShowLoginPage(request):
    return render(request,"video_analytics_app/login_page.html")


def LoginUser(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request,"video_analytics_app/login_page.html")
    else:
        return HttpResponseRedirect("/homepage")

def doLogin(request):
    AUTH_USER_MODEL = "video_analytics_app.analytics_users"
    print("Hi")
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username,password=password)  # Passing Username and Password in authenticate
        #login(request, admin)  # Calling the login function and passing request and our user object
        """if user.is_superuser:
           print("This is a superuser")"""
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/homepage')
        else:
            print("Invalid Login Details: {0} , {1}".format(username, password))
            return HttpResponse("Invalid Login Details")

def authenticateUser(username, password):
    print("Username:" + username)
    try:
        user = analytics_users.objects.filter(username=username,password=password).first()
        print(user)
    except analytics_users.DoesNotExist:
        user = None
        print("exception occured")
    return user


def HomePage(request):
    return render(request,'video_analytics_app/homepage.html')

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect('/login_user')


def addData(request):
    if request.user.is_superuser:
        return render(request,'video_analytics_app/add_video.html')
    else:
        return HttpResponse("<h2>You do not have access to this feature</h2>")


def AddVideo(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.is_superuser:
            try:
                vide = video(title=request.POST.get('title', ''), embed_code=request.POST.get('embed_code', ''))
                vide.save()
                messages.success(request, "Added Successfully")
            except Exception as e:
                print(e)
                messages.error(request, "Failed to Add Data")
        else:
            return HttpResponse("<h2>You do not have access to this feature</h2>")
    return HttpResponseRedirect("/addData")


def ViewVideo(request):
    all_video = video.objects.all()
    return render(request, 'video_analytics_app/video_showing.html',{'videos':all_video})


def VideoChart(request):
    if request.user.is_superuser:
        all_title = video.objects.all()

        # vidtitle = ['Title1', 'Title2', 'Title3', 'Title4', 'Title5']
        # vidwatchcount = [3, 5, 1, 6, 9]
        vidtitle = '|'.join([x.title for x in all_title])
        vidwatchcount = '|'.join([str(x.users_watched_count) for x in all_title])
        return render(request, 'video_analytics_app/chart.html',{'videoTitles': vidtitle, 'videoUserWatchedCount': vidwatchcount})
    else:
        return HttpResponse("<h2>You do not have access to this feature</h2>")


def AddVideoAnalytics(request):
    all_vid = video.objects.all()
    for vid in all_vid:
        if vid.viewed_by_users != '':
            viewed_by_users = json.loads(vid.viewed_by_users)
        else:
            viewed_by_users = []
        if request.user.id in viewed_by_users:
            continue
        viewed_by_users.append(request.user.id)
        vid.viewed_by_users = json.dumps(viewed_by_users)
        vid.users_watched_count = vid.users_watched_count + 1
        vid.save()
    data = {'analytics_record': True}
    return JsonResponse(data)
