from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'recruitments.views.home', name='home'),
    url(r'^results$', 'recruitments.views.results_view', name='home'),
	url(r'^submit$', 'recruitments.views.submit_resume', name='submission'),
	url(r'^submission_success$', 'recruitments.views.submit_success', name='submission_success'),
	url(r'^evaluate$', 'recruitments.views.evaluate_view', name='evaluation_main'),
	url(r'^evaluation_success$', 'recruitments.views.evaluate_success', name='evaluation_success'),
	url(r'^evaluate/(?P<resume_id>\w{0,50})$', 'recruitments.views.evaluate_resume', name='evaluation'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
