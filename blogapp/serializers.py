__author__ = 'riccardo'
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User, Group
from models import BlogArticle

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BlogArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='user-detail', format='json')
    class Meta:
        model = BlogArticle
        fields = ('title', 'blog_content', 'author')
