from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'(?P<slug>.+)/$', 'SIG.views.sig_view', name='sig_landing'),
)