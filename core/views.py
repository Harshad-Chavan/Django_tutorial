from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer



# Create your views here.
def test_view(request):
    data = {

        'Name': 'jhon',
        'age' : 23,

    }
    return JsonResponse(data)


class PostView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
        serializer_class = PostSerializer
        queryset = Post.objects.all()

        def get(self,request,*args,**kwargs):
             return self.list(request,*args,**kwargs)

        def post(self,request,*args,**kwargs):
            return self.create(request,*args,**kwargs)




# class Rest_test_view(APIView):

#     permissions_classes = (IsAuthenticated,)

#     def get(self,request,*args,**kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs,many = True)
#         return Response(serializer.data)


#     def post(self,request,*args,**kwargs):
#         serializer = PostSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)