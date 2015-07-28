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
	return render(request, 'flatpages/landing.html', {})
	
def submit_resume(request):
	if request.method == 'GET':
		form = forms.FillResumeForm()
	else:
		form = forms.FillResumeForm(request.POST)
		
		if form.is_valid():
			new_resume = form.save()
			new_resume.current_round = 'Pending Resume Evaluation'
			new_resume.save()
			return render_to_response('flatpages/submission_success.html')
	return render_to_response('flatpages/form_layout.html',{'title': "Candidate resume form" ,'ResumeForm':form},context_instance=RequestContext(request))

@login_required
def evaluate_view(request):
	return render(request, 'flatpages/resumes_to_be_evaluated.html', {"resumes":models.Resume.objects.exclude(qualified_for_round=0).exclude(qualified_for_round=5).order_by('name').order_by('current_round')})

@login_required
def evaluate_resume(request,resume_id):
	rounds = ['Not Qualified','Pending Resume Evaluation','Personal Interview','Group Discussion','Final Interview','Selected']
	
	resume_id = request.GET['resume_id']
	#in case the url has a trailing '/', in which case the resume_id will contain the slash as well
	try:
		int(resume_id)
	except ValueError:
		resume_id = resume_id[:-1]
	
	if request.method == 'GET':
		form = forms.EvaluateResumeForm()
		resume_to_be_evaluated = models.Resume.objects.get(id=resume_id)

	else:
		form = forms.EvaluateResumeForm(request.POST)
		
		if form.is_valid():
			current_resume = models.Resume.objects.get(id=resume_id)
			current_resume.score = request.POST['score']
			current_resume.comments = request.POST['comments']
			current_resume.informal_comments = request.POST['informal_comments']
			if 'qualified' in request.POST:
				current_resume.qualified = True
				current_resume.qualified_for_round += 1
			else:
				current_resume.qualified = False
				current_resume.qualified_for_round = 0

			current_resume.current_round = rounds[current_resume.qualified_for_round]
			current_resume.evaluated_by = request.user.username
			current_resume.save()

			return render_to_response('flatpages/evaluation_success.html')
	return render_to_response('flatpages/evaluation_form_layout.html',{'evaluationForm':form,'resume':models.Resume.objects.get(id=resume_id)},context_instance=RequestContext(request))
	
def results_view(request):
	return render(request, 'flatpages/results.html', {"resumes":models.Resume.objects.all().order_by('name')})