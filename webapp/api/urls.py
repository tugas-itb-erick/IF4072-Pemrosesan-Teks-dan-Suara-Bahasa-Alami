from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('search/', views.search, name='search'), # resp: users with keyword / posts with tag
    path('user/<int:user_id>/', views.user, name='user'), # resp: user feed
    # path('post/<int:post_id>/', views.post, name='post') 
]