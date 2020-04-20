# chat/urls.py
from django.urls import path
from .views import index,room

appname = 'chat'
urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]