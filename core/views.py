from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def test_view(request):
    data = {

        'Name': 'jhon',
        'age' : 23,

    }
    return JsonResponse(data)

class Rest_test_view(APIView):
    def get(self,request,*args,**kwargs):
        data = {
            'Name': 'jhon',
            'age' : 23,
        }
        return Response(data)