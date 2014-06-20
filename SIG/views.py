from django.http import Http404
from django.shortcuts import render

from SIG.models import SIGroup

# Create your views here.
def sig_view(request, slug):
	print "slug is " + slug
	try:
		sig = SIGroup.objects.get(slug=slug)
	except SIGroup.DoesNotExist:
		raise Http404

	return render(request, 'group.html', { 'sig' : sig})