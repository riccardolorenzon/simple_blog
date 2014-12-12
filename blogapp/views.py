from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
