from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('search/', views.search, name='search'), # resp: users with keyword / posts with tag
    path('user/<str:username>/', views.user, name='user'), # get user info by user_id is deprecated jdi routingnya agak aneh ya :(
    path('user/<int:user_id>/feed', views.user_feed, name='user_feed'), # resp: user feed
    # path('post/<int:post_id>/', views.post, name='post') 
]