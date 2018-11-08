import json

from django.http import HttpResponse
from django.shortcuts import render
from instagram_web_api import Client
from . import errors
from .enums.search_type import SeachType

def index(request):    
    api = create_api_client(request)
    return render(request, 'index.html')
    # return HttpResponse(api.settings) # serialize byte??

def search(request):
    try:
        query, search_type = validate_search(request)
    except ValueError:
        return HttpResponse(content=errors.INVALID_QUERY, content_type="application/json", status=404)

    api = create_api_client(request)
    if search_type == SeachType.TAG:
        search_result = search_by_tag(api, query)
        # return render(request, 'posts.html', context=json.dumps(search_result))
        return ""
    else:
        search_result = search_by_username(api, query)
        return render(request, 'profiles.html', { 'query': query, 'profiles': search_result })
    # return HttpResponse(content=json.dumps(search_result), content_type="application/json")

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
    attr = ["username", "full_name", "is_private", "profile_picture"]
    user_dict = {}
    for key, val in user.items():
        if key in attr:
            user_dict[key] = val
    key_edge = "edge_owner_to_timeline_media"
    if key_edge in user.keys():
        user_dict[key_edge] = parse_edge_timeline_media(user.get(key_edge, {}))
    return user_dict

def parse_edge_timeline_media(edge):
    new_edge = {"count": edge.get("count"), "page_info": edge.get("page_info")}
    new_edge["media"] = [{
        "created_time": el.get("node", {}).get("taken_at_timestamp"), 
        "shortcode": el.get("node", {}).get("shortcode"), 
        "display_url": el.get("node", {}).get("display_url")
        } for el in edge.get("edges", {})
    ]
    return new_edge

def user(request, username): 
    api = create_api_client(request)
    user = api.user_info2(username)
    return render(request, 'posts.html', context=parse_user(user))
    # return HttpResponse(content=json.dumps(parse_user(user)), content_type="application/json")

def user_media(request, shortcode):
    api = create_api_client(request)
    media = api.media_info2(shortcode)
    media = parse_user_media(media)
    return HttpResponse(content=json.dumps(media), content_type="application/json")

def parse_user_media(media):
    attr = ["created_time", "shortcode", "display_url"]
    media_dict = {}
    for key, val in media.items():
        if key in attr:
            media_dict[key] = val
    media_dict["caption"] = media.get("caption", {}).get("text")
    media_dict["carousel_display_urls"] = parse_carousel(media.get("carousel_media", {}))
    media_dict["edge_media_to_comment"] = parse_comments(media.get("edge_media_to_comment", {}))
    return media_dict

def parse_carousel(carousel):
    return [media.get("display_url") for media in carousel]

def parse_comments(comments):
    comments_dict = {
        "count": comments["count"], 
        "page_info": comments["page_info"]
    }
    arr_comments = []
    for el in comments.get("edges", {}):
        node = el.get("node", {})
        comment = {
            "created_time": node.get("created_at"), 
            "text": node.get("text"), 
            "username": node.get("owner", {}).get("username"), 
            "profile_picture": node.get("owner", {}).get("profile_pic_url")
        }
        comment["hate_score"] = analyze_comment(comment["text"])
        arr_comments.append({"comment": comment})
    comments_dict["comments"] = arr_comments
    return comments_dict
        
def analyze_comment(text):
    # gunakan model
    physic = 0
    race = 0
    religion = 0
    return {"physic": physic, "race": race, "religion": religion}

def create_api_client(request):
    if request.COOKIES.get("hate_speech_analyzer"):
        try:
            api = Client(settings=json.loads(request.COOKIES.get("hate_speech_analyzer")))
        except Exception:
            api = Client(auto_patch=True, drop_incompat_keys=False)
    else:
        api = Client(auto_patch=True, drop_incompat_keys=False)
    return api

