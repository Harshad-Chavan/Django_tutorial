from django.urls import path
from .views import IndexView

appname = 'weather'
urlpatterns = [
    path('',IndexView.as_view(),name = 'index')
    

]