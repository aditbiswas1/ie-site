from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'recruitments.views.home', name='home'),
    url(r'^results$', 'recruitments.views.results_view', name='home'),
	url(r'^submit$', 'recruitments.views.submit_resume', name='submission'),
	url(r'^evaluate$', 'recruitments.views.evaluate_view', name='evaluation_main'),
	url(r'^evaluate/(?P<resume_id>\w{0,50})$', 'recruitments.views.evaluate_resume', name='evaluation'),
    url(r'^pi$', 'recruitments.views.get_pi', name='pi_list'),
    url(r'^gd$', 'recruitments.views.get_gd', name='gd_list'),
    url(r'^evaluate_pigd/(?P<resume_id>\w{0,50})$', 'recruitments.views.evaluate_pigd', name='evaluate_pigd'),
    url(r'^evaluations', 'recruitments.views.get_eval', name='get_eval'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
