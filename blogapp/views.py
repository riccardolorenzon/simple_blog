from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle
from django.contrib.auth import authenticate, login

# Create your views here
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        if user != None:
            login(request,user)
            response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : BlogArticle.objects.all(), "user" : user} )
            return response
    response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : BlogArticle.objects.all()} )
    return response

def createblog(request):
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return HttpResponseRedirect('/')