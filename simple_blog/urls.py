from django.conf.urls import patterns, include, url
from blogapp import views
from blogapp.views import UserViewSet, GroupViewSet, BlogArticleViewSet
from django.contrib import admin
from rest_framework import routers
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'blogarticles', BlogArticleViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'home'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createblog),
    url(r'^edit-article/(?P<article_id>\w+)/$', views.edit_article),
    url(r'^update-article/(?P<article_id>\w+)/$', views.update_article),
    url(r'^delete-article/(?P<article_id>\w+)/$', views.delete_article),
    url(r'^upload-image/$', views.upload_image, name = 'upload'),
    url(r'^delete-image/(?P<article_id>\w+)/images/(?P<image_id>\w+)/$', views.delete_image),
    url(r'^logout/', views.logout_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()