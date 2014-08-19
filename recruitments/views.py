from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from recruitments import forms,models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
	print "users:"
	print User.objects.all()
	return render(request, 'flatpages/landing.html', {})
	
def submit_resume(request):
	if request.method == 'GET':
		form = forms.FillResumeForm()
	else:
		form = forms.FillResumeForm(request.POST)
		
		if form.is_valid():
			new_resume = form.save()
			return render_to_response('flatpages/submission_success.html')
	return render_to_response('flatpages/form_layout.html',{'ResumeForm':form},context_instance=RequestContext(request))

@login_required
def evaluate_view(request):
	return render(request, 'flatpages/resumes_to_be_evaluated.html', {"resumes":models.Resume.objects.exclude(qualified_for_round='selected')})

@login_required
def evaluate_resume(request,resume_id):
	if request.method == 'GET':
		form = forms.EvaluateResumeForm()
	else:
		form = forms.EvaluateResumeForm(request.POST)
		if form.is_valid():
			resume_id = request.GET['resume_id']
			#in case the url has a trailing '/', in which case the resume_id will contain the slash as well
			try:
				int(resume_id)
			except ValueError:
				resume_id = resume_id[:-1]
			current_resume = models.Resume.objects.get(id=resume_id)
			current_resume.score = request.POST['score']
			current_resume.comments = request.POST['comments']
			current_resume.informal_comments = request.POST['informal_comments']
			current_resume.evaluated_by = request.POST['evaluated_by']
			current_resume.qualified_for_round = request.POST['qualified_for_round']
			current_resume.save()
			return render_to_response('flatpages/evaluation_success.html')
	return render_to_response('flatpages/form_layout.html',{'ResumeForm':form,'ResumeId':request.GET['resume_id']},context_instance=RequestContext(request))
	
def results_view(request):
	return render(request, 'flatpages/results.html', {"resumes":models.Resume.objects.all()})