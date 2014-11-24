from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover
from igoda.views import getWeb
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^igoda/getWeb/$','igoda.views.getWeb'),    
    #url(r'^igoda/get/$','igoda.views.get_number'),
    url(r'^admin/', include(admin.site.urls)),
)
