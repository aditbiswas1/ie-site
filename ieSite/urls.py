from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'ieSite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bootcamp/', include('bootcamp.urls')),
    url(r'^sig/', include('SIG.urls')),
)

# static page placeholders can be created and added uner flatpages
urlpatterns += patterns('',
    (r'^pages/', include('django.contrib.flatpages.urls')),
)
