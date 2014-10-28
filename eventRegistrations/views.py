from django.shortcuts import render,render_to_response,get_object_or_404
from eventRegistrations import forms,models
from django.template import RequestContext
# Create your views here.

def regForm(request,eventSlug):
    event = get_object_or_404(models.Event,slug=eventSlug)
    if request.method == 'GET':
        form = forms.RegistrationForm()
    else:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            members = form.cleaned_data['members']
            contact_number = form.cleaned_data['contact_number']
            alternate_contact_number = form.cleaned_data['alternate_contact_number']
            newReg = models.Registration(
                    event=event,
                    members=members,
                    contact_number=contact_number,
                    alternate_contact_number=alternate_contact_number,
                    )
            newReg.save()
            return render_to_response('flatpages/submission_success.html')
    return render_to_response('flatpages/events_form_layout.html',
            {'form':form,
                'event':event,
            },
            context_instance=RequestContext(request)
            )

def eventsHome(request):
    events = models.Event.objects.all()
    return render_to_response('flatpages/events_home.html',
            {'events':events},
            context_instance=RequestContext(request)
            )

def eventPage(request,slug):
    event = get_object_or_404(models.Event,slug=slug)
    rounds = models.Round.objects.filter(event=event).order_by('round_no')
    return render_to_response(
            'flatpages/event_page.html',
            {
            'event':event,
            'rounds':rounds,
            },
            context_instance=RequestContext(request)
            )
