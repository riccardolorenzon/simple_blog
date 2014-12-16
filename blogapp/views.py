from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, BlogArticleSerializer

# index
def index(request):
    blog_objects = BlogArticle.objects.all()
    paginator = Paginator(blog_objects, 5)
    page = request.GET.get('page')
    try:
        blog_objects = paginator.page(page)
    except PageNotAnInteger:
        blog_objects = paginator.page(1)
    except EmptyPage:
        blog_objects = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)

        if user != None:
            login(request,user)
            response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : blog_objects, "user" : user} )
            return response
    response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : blog_objects} )
    return response

# create blog view
def createblog(request):
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return HttpResponseRedirect('/')

def edit_article(request, article_id):
    return HttpResponse("edit")

def delete_article(request, article_id):
    return HttpResponse("delete")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogArticleViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer