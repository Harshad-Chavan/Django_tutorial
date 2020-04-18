from django.urls import path

from . import views
# from .views import Rest_test_view
from .views import PostView


app_name = 'core'
urlpatterns = [
    # ex: /cores/test
    
    path('test/', views.test_view, name='test'),
    #path('rest_test/',Rest_test_view.as_view(),name='rest_test')
    path('rest_test/',PostView.as_view(),name='rest_test')
    

    
]