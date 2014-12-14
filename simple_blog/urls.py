from django.conf.urls import patterns, include, url
from blogapp import views
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
