from django.conf.urls import patterns, include, url
from blogapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createblog),
    url(r'^logout/', views.logout_view),

)
