from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'akademik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^login/', include(admin.site.urls)),
)
