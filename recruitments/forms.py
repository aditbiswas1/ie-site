from django import forms
from recruitments import models
from SIG.models import SIGroup
from django.forms.widgets import CheckboxSelectMultiple

#form to be used by candidates to submit resumes
class FillResumeForm(forms.ModelForm):
	
    def __init__(self, *args, **kwargs): 
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name *"
        self.fields['roll_number'].label = "Roll Number * (eg. 14CO02)"
        self.fields['gender'].label = "Gender *"
        self.fields['phone_number'].label = "Phone Number * (10 digits)"
        self.fields['email_id'].label = "Email ID *"
        self.fields['about_me'].label = "Tell us about yourself. *"
        self.fields['why_ie'].label = "Tell us why you'd like to be a part of IE. *"
        self.fields['event_participation'].label = "Have you participated in IE events? How was your experience? *"
        self.fields['event_participation'].required = True
        self.fields['core_sig_choice'].label = "What Core SIG(s) would you like to be a part of? *"
        self.fields['core_sig_choice'].widget = CheckboxSelectMultiple()
        self.fields['core_sig_choice'].queryset = SIGroup.objects.exclude(core=False)
        self.fields['core_sig_interests'].label = "Tell us, briefly, why these SIG(s) interest you. *"
        self.fields['core_sig_projects'].label = "Have you done any work relevant to the SIGs you chose?"
        self.fields['core_sig_projects'].required = False
        self.fields['next_tech'].label = "What technology do you think is the next big thing?"
        self.fields['next_tech'].required = False
        self.fields['aux_sig_choice'].label = "What Auxiliary SIG(s) would you like to be a part of?"
        self.fields['aux_sig_choice'].widget = CheckboxSelectMultiple()
        self.fields['aux_sig_choice'].queryset = SIGroup.objects.exclude(core=True)
        self.fields['aux_sig_choice'].required = False
        self.fields['aux_sig_interests'].label = "Do you have any ideas for new SIGs or projects? Please explain."
        self.fields['aux_sig_interests'].required = False
        self.fields['witty_question'].label = "If you're awarded a death penalty for being late for an IE meeting, what would your last words be?"
        self.fields['witty_question'].required = False
        self.fields['picture'].label = "Tell us what thoughts come to mind when you see the picture below."
        self.fields['picture'].required = False

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
            'event_participation',
            'core_sig_choice',
            'core_sig_interests',
            'core_sig_projects',
            'next_tech',
            'aux_sig_choice',
            'aux_sig_interests',
            'witty_question',
            'picture'
        ]


#form to be used by members to grade resumes
class EvaluateResumeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs): 
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['score'].label = "Score *"
        self.fields['comments'].label = "Break-up of Score *"
        self.fields['informal_comments'].label = "Impression of the Candidate(compulsory)/Informal Comments/P.M.S. *"
        self.fields['qualified'].label = "Qualified *"
        self.fields['qualified'].required = False
        self.fields['sig_evaluators'].label = "Name of the evaluator and SIG (for PIs, enter name of the SIG the candidate qualifies for and the name of the person who took the SIG-specific interview. for GDs, just enter the name of the evaluator.) *"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.ResumeEvaluation
        fields = [
            'score',
            'informal_comments',
            'comments',
            'qualified',
            'sig_evaluators'
        ]
