import json

from django.http import HttpResponse
from django.shortcuts import render

from instagram_web_api import Client

# Create your views here.
def index(request):
    api = create_api_client(request)
    return HttpResponse(api.settings) # serialize byte??

def search(request):
    return HttpResponse("Search")

def user(request, user_id): 
    return HttpResponse("User " + str(user_id))

def create_api_client(request):
    if request.COOKIES.get('iganalyzer'):
        try:
            api = Client(settings=json.loads(request.COOKIES.get('iganalyzer')))
        except Exception:
            api = Client(auto_patch=True, drop_incompat_keys=False)
    else:
        api = Client(auto_patch=True, drop_incompat_keys=False)
    return api