from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',

    url(r'^(?P<slug>[^/]+)/$','eventRegistrations.views.eventPage',name = 'event_page'),
    url(r'^(?P<eventSlug>[^/]+)/register/$','eventRegistrations.views.regForm',name = 'reg_form'),
    url(r'^$','eventRegistrations.views.eventsHome',name = 'events_home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
