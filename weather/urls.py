from django.urls import path
from .views import index_view,IndexView

appname = 'weather'
urlpatterns = [
    path('',IndexView.as_view(),name = 'index')
    

]