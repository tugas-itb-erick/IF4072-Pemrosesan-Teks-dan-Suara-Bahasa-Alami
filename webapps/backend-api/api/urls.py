from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('search/', views.search, name='search'), # resp: users with keyword / posts with tag
    path('user/<str:username>/', views.user, name='user'), # get user info by user_id is deprecated jdi routingnya agak aneh ya :(
    path('media/<str:shortcode>', views.user_media, name='user_media')
]