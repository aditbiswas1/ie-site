from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.core.context_processors import csrf
from django.template import RequestContext
from recruitments import forms, models
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
			new_resume.save()
			return redirect('/recruitment/submission_success')
	return render_to_response('flatpages/form_layout.html',{'resume_form':form,'image':'{{ STATIC_URL }}img/picture_question.jpg'},context_instance=RequestContext(request))

@login_required
def evaluate_view(request):
	return render(request, 'flatpages/resumes_to_be_evaluated.html', {"resumes":models.Resume.objects.exclude(qualified_for_round=0).exclude(qualified_for_round=5).order_by('name','current_round')})

@login_required
def evaluate_resume(request,resume_id):
	rounds = ['Not Qualified','Resume Evaluation Started','Personal Interview','Group Discussion','Final Interview','Selected']
	
	resume_id = request.GET['resume_id']
	#in case the url has a trailing '/', in which case the resume_id will contain the slash as well
	try:
		int(resume_id)
	except ValueError:
		resume_id = resume_id[:-1]
	
	current_resume = models.Resume.objects.get(id=resume_id)
	
	if request.method == 'GET':
		form = forms.EvaluateResumeForm()
	else:
		form = forms.EvaluateResumeForm(request.POST)
		
		if form.is_valid():
			new_evaluation = form.save(commit=False)
			new_evaluation.resume = current_resume
			new_evaluation.score = request.POST['score']
			new_evaluation.comments = request.POST['comments']
			new_evaluation.informal_comments = request.POST['informal_comments']
			new_evaluation.evaluated_by = request.user
			new_evaluation.name = current_resume.name
			if 'qualified' in request.POST:
				new_evaluation.qualified = True
				new_evaluation.save()
				print models.ResumeEvaluation.objects.filter(resume=current_resume,qualified=True)
				#for resume round, pass the candidate only if 2 people pass the candidate, but for other rounds, one is sufficient
				if (current_resume.qualified_for_round == 1 and models.ResumeEvaluation.objects.filter(resume=current_resume,qualified=True).__len__() == 2) or (current_resume.qualified_for_round > 1 and current_resume.qualified_for_round < 5):
					current_resume.qualified_for_round += 1
			else:
				new_evaluation.qualified = False
				new_evaluation.save()
				#for resume round, fail the candidate only if 2 people fail the candidate, but for other rounds, one is sufficient
				if (current_resume.qualified_for_round == 1 and models.ResumeEvaluation.objects.filter(resume=current_resume).exclude(qualified=True).__len__() == 2) or (current_resume.qualified_for_round > 1 and current_resume.qualified_for_round < 5):
					current_resume.qualified_for_round = 0

			current_resume.current_round = rounds[current_resume.qualified_for_round]
			new_evaluation.current_round = current_resume.current_round
			new_evaluation.save()
			current_resume.save()
			return redirect('/recruitment/evaluation_success')
	return render_to_response('flatpages/form_layout.html',{'resume_form':form,'resume':current_resume},context_instance=RequestContext(request))
	
def results_view(request):
	result_list = []
	for eval in models.ResumeEvaluation.objects.all().order_by('name'):
		if eval.current_round == eval.resume.current_round:
			result_list.append(eval)
	return render(request, 'flatpages/results.html', {"resumes":result_list})
	
def submit_success(request):
	return render(request,'flatpages/submission_success.html')
	
def evaluate_success(request):
	return render(request,'flatpages/evaluation_success.html')