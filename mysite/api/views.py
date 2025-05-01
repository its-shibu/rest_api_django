from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost, FormData
from .serializers import BlogPostSerializer
from .serializers import FormDataSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FormDataListCreate(generics.ListCreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer

    def delete(self, request, *args, **kwargs):
        FormData.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormDataRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormData.objects.all()
    serializer_class= FormDataSerializer
    lookup_field = 'pk'


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'


class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', "")
        if title:
            blog_posts = BlogPost.objects.filter(title__incontains = title)
        else: 
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


