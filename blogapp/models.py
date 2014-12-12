from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length=60)
    blog_content = models.TextField()
    author = models.ForeignKey(User)

class ImageBlogArticle(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='./images/')
    blogarticle = models.ForeignKey(BlogArticle)

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    blogarticles = models.ManyToManyField(BlogArticle)
