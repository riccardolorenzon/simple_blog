from django.conf.urls import patterns, include, url
from blogapp import views
from blogapp.views import UserViewSet
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', UserViewSet)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'home'),
    url(r'^api/users', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createblog),
    url(r'^logout/', views.logout_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
