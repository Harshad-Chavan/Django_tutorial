from rest_framework import serializers

from .models import Post

from django import forms

# this is an exmaple form that we will use whike making forms
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = {'title','description'}

# a serializers has a same structure as basic form use this serializer in a view
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','owner']
