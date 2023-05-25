from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome")

def user_details(request, name):
    return HttpResponse(f"<h1>hello {name}</h1>")