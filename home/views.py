from urllib import request
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")

def work(request):
    return HttpResponse("Work")

def mission(request):
    return HttpResponse("Mission")

def team(request):
    return HttpResponse("Team")

def state(request):
    return HttpResponse("State")

def achieve(request):
    return HttpResponse("Achieve")

def donate(request):
    return HttpResponse("Donate")

def job(request):
    return HttpResponse("Job")

def login(request):
    return HttpResponse("Login")
