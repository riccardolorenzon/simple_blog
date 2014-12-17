from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle, ImageBlogArticle
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
    blog = BlogArticle.objects.get(id = article_id)
    return render(request, "./blogedit.html", {"blog" : blog})

def update_article(request, article_id):
    blog = BlogArticle.objects.get(id = article_id)
    if blog != None and request.method == 'POST':
        blog.title = request.POST['title']
        blog.blog_content = request.POST['content']
        blog.save()
    return HttpResponseRedirect("/")

def delete_article(request, article_id):
    blog = BlogArticle.objects.filter(id = article_id)
    deleted = True
    if blog == None:
        deleted = False
    else:
        blog.delete()
    return HttpResponseRedirect("/")

def upload_image(request):
    new_sharedimage = ImageBlogArticle()
    new_sharedimage.image = request.FILES['file']
    new_sharedimage.blogarticle_id = request.POST['blogArticleId']
    new_sharedimage.title = request.POST['title']
    new_sharedimage.description = request.POST['description']
    new_sharedimage.save()
    return HttpResponseRedirect("/")

def delete_image(request, article_id, image_id):
    image = ImageBlogArticle.objects.get(id = image_id)
    image.delete()
    return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogArticleViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer