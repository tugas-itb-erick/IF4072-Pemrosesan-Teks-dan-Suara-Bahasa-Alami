import json

from django.http import HttpResponse
from django.shortcuts import render
from . import errors
from instagram_web_api import Client

# Create your views here.
def index(request):
    api = create_api_client(request)
    return HttpResponse(api.settings) # serialize byte??

def search(request):
    api = create_api_client(request)
    query = request.GET.get('query', '')
    search_type = request.GET.get('type', 'username')
    if query == '':
        print(errors.INVALID_QUERY)
        return HttpResponse(content=errors.INVALID_QUERY, content_type='application/json', status=404)
    
    if search_type == 'tag':
        pass # TBD
    else: # search_type == 'username'
        search_result = api.search(query)["users"]
        users = [result["user"] for result in search_result]
        del_list = ["profile_pic_id", "is_verified", "has_anonymous_profile_picture", 
        "follower_count", "reel_auto_archive", "byline", "social_context", "search_social_context", 
        "mutual_followers_count", "following", "outgoing_request", "profile_pic_url", "unseen_count"]
        for user in users:
            for key in del_list:
                user.pop(key, None)
        users = json.dumps(users)
    return HttpResponse(content=users, content_type='application/json')

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