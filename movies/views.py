import re
import json
import requests

API_KEY = '444ddd63'

from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    template = loader.get_template("movies/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def details(request, imdbID):
    template = loader.get_template("movies/details.html")
    response = requests.get(f'http://www.omdbapi.com/?apikey={API_KEY}&i={imdbID}') 
    match= response.json()
    return HttpResponse(template.render({ "details": match }, request))

def search(request, query):
    response = requests.get('http://www.omdbapi.com/?apikey=444ddd63&s=' + query) 
    matches = response.json()['Search']
    return JsonResponse(matches, safe=False)
