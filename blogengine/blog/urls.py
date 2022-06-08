
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('<str:slug>/', post_detail, name='post_detail_url')
]