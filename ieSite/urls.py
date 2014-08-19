from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'ieSite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bootcamp/', include('bootcamp.urls')),
    url(r'^sig/', include('SIG.urls')),
	url(r'^recruitment/', include('recruitments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'projects/(?P<projectslug>[^/]+)/$','SIG.views.project_view',name = 'projects'),
    url(r'articles/(?P<articleslug>[^/]+)/$','SIG.views.article_view',name = 'articles'),
)

# static page placeholders can be created and added under flatpages
urlpatterns += patterns('',
    (r'^pages/', include('django.contrib.flatpages.urls')),
)
