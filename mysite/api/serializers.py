from rest_framework import serializers
from .models import BlogPost
from .models import FormData


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']


class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ['id', 'name', 'email', 'message', 'address', 'phone_number']