import json

from django.http import HttpResponse
from django.shortcuts import render
from instagram_web_api import Client
from . import errors
from .enums.search_type import SeachType

def index(request):    
    api = create_api_client(request)
    return HttpResponse(api.settings) # serialize byte??

def search(request):
    try:
        query, search_type = validate_search(request)
    except ValueError:
        return HttpResponse(content=errors.INVALID_QUERY, content_type="application/json", status=404)

    api = create_api_client(request)
    if search_type == SeachType.TAG:
        search_result = search_by_tag(api, query)
    else:
        search_result = search_by_username(api, query)
    return HttpResponse(content=json.dumps(search_result), content_type="application/json")

def validate_search(request):
    query = request.GET.get("query", "")
    search_type = request.GET.get("type", "")
    if query == "":
        raise ValueError("Username must not be empty")
    if search_type not in SeachType.list_values():
        raise ValueError("Tag must be one of these: {}".format(SeachType.list_values()))
    return query, search_type

def search_by_tag(api, tag):
    search_result = api.search(tag)["hashtags"]
    return search_result

def search_by_username(api, username):
    search_result = api.search(username)["users"]
    users = [result["user"] for result in search_result]
    return parse_users(users)

def parse_users(users):
    new_users = []
    for user in users:
        new_users.append(parse_user(user))
    return new_users
def parse_user(user):
    attr = ["pk", "username", "full_name", "is_private", "profile_picture"]
    user_dict = {}
    for key, val in user.items():
        if key in attr:
            user_dict[key] = val
    return user_dict

def user(request, user_id): 
    api = create_api_client(request)
    user_feed = api.user_feed(user_id) # TODO: Pagination
    return HttpResponse(content=json.dumps(parse_user_feed(api, user_feed)), content_type="application/json")

def parse_user_feed(api, user_feed):
    # get all media's shortcode
    shortcodes = []
    for post in user_feed:
        shortcodes.append(post["node"]["shortcode"])
    # get all media's comments
    comments = []
    for shortcode in shortcodes:
        comments.append(api.media_comments(shortcode)) # TODO: Pagination
    return comments

def create_api_client(request):
    if request.COOKIES.get("hate_speech_analyzer"):
        try:
            api = Client(settings=json.loads(request.COOKIES.get("hate_speech_analyzer")))
        except Exception:
            api = Client(auto_patch=True, drop_incompat_keys=False)
    else:
        api = Client(auto_patch=True, drop_incompat_keys=False)
    return api

