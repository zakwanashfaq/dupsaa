from django.shortcuts import render
from django.http import request, HttpResponse


# Create your views here.

def homepage(request):
    return HttpResponse('Hello')