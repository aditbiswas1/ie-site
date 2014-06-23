from django.http import Http404
from django.shortcuts import render, get_object_or_404

from SIG.models import SIGroup,Project,Article

# Create your views here.
def sig_view(request, slug):
    print "slug is " + slug
    try:
	    sig = SIGroup.objects.get(slug=slug)
    except SIGroup.DoesNotExist:
	    raise Http404

    return render(request, 'group.html', { 'sig' : sig})

def project_view(request,projectslug):
    print "project slug is " + projectslug
    project = get_object_or_404(Project,slug=projectslug)
    return render(request, 'project.html',{'project':project})

def article_view(request,articleslug):
    print "article slug is " + articleslug
    article = get_object_or_404(Article,slug=articleslug)
    return render(request,'article.html',{'article':article})

