from django import forms
from recruitments import models
from SIG.models import SIGroup
from django.forms.widgets import CheckboxSelectMultiple

#form to be used by candidates to submit resumes
class FillResumeForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs): 
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Name*"
		self.fields['roll_number'].label = "Roll Number* (eg. 11CO02)"
		self.fields['gender'].label = "Gender*"
		self.fields['phone_number'].label = "Phone Number* (10 digits)"
		self.fields['email_id'].label = "Email ID*"
		self.fields['about_me'].label = "Tell us about yourself.*"
		self.fields['why_ie'].label = "Tell us why you'd like to be a part of IE.*"
		self.fields['why_not_you'].label = "Why should we NOT take you?*"
		self.fields['core_sig_choice'].label = "What Core SIG(s) would you like to be a part of?*"
		self.fields['core_sig_choice'].widget = CheckboxSelectMultiple()
		self.fields['core_sig_choice'].queryset = SIGroup.objects.exclude(core=False)
		self.fields['core_sig_interests'].label = "Tell us, briefly, why these SIG(s) interest you.*"
		self.fields['core_sig_projects'].label = "Have you done any work relevant to the SIGs you chose before?"
		self.fields['core_sig_projects'].required = False
		self.fields['aux_sig_choice'].label = "What Auxiliary SIG(s) would you like to be a part of?"
		self.fields['aux_sig_choice'].widget = CheckboxSelectMultiple()
		self.fields['aux_sig_choice'].queryset = SIGroup.objects.exclude(core=True)
		self.fields['aux_sig_choice'].required = False
		self.fields['aux_sig_interests'].label = "Briefly explain why you'd like to be a part of the auxiliary SIG(s) you chose."
		self.fields['aux_sig_interests'].required = False
		self.fields['witty_question'].label = "If you're awarded a death penalty for being late for an IE meeting, what would your last words be?*"
		self.fields['picture'].label = "Tell us what thoughts come to mind when you see the picture below.*"
	
	def clean(self):
		return self.cleaned_data
		
	class Meta:
		model = models.Resume
		fields = [
			'name',
			'roll_number',
			'gender',
			'phone_number',
			'email_id',
			'about_me',
			'why_ie',
			'why_not_you',
			'core_sig_choice',
			'core_sig_interests',
			'core_sig_projects',
			'aux_sig_choice',
			'aux_sig_interests',
			'witty_question',
			'picture'
		]
	

#form to be used by members to grade resumes
class EvaluateResumeForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs): 
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		self.fields['informal_comments'].label = "Impression of the Candidate(compulsory)/Informal Comments/P.M.S.*"
		self.fields['score'].label = "Score*"
		self.fields['comments'].label = "Break-up of Score*"
		self.fields['qualified'].label = "Qualified*"
		self.fields['qualified'].required = False
	
	def clean(self):
		return self.cleaned_data
	
	class Meta:
		model = models.Resume
		fields = [
			'score',
			'informal_comments',
			'comments',
			'qualified'
		]