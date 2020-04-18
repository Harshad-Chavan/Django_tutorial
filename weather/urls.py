from django.urls import path
from .views import index_view

appname = 'weather'
urlpatterns = [

    path('',index_view,name = 'index')
]