from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'(?P<slug>[^/]+)/$', 'SIG.views.sig_view', name='sig_landing'),
    url(r'projects/(?P<projectslug>[^/]+)/$','SIG.views.project_view',name = 'sig_projects'),
    url(r'articles/(?P<articleslug>[^/]+)/$','SIG.views.article_view',name = 'sig_articles'),

)
