from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Hello world', content_type='text/plain')

