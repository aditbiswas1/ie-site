from django.db import models
from SIG.models import SIGroup
from datetime import datetime
from django.contrib.auth.models import User

#model to contain the answers to the questions in the form to be filled in by candidates
class Resume(models.Model):

    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
    )

    CORE_CHOICES = (
        ('code','Code'),
        ('gadget','Gadget'),
        ('garage','Garage'),
        ('finance','Finance'),
    )

    AUX_CHOICES = (
        ('film','Film'),
        ('vriddhi','Vriddhi'),
    )

    #TODO: Separate scoring and submitted attributes to avoid concurrency issues

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    email_id = models.EmailField(max_length=254)
    about_me = models.TextField(max_length=400)
    why_ie = models.TextField(max_length=400)
    event_participation = models.TextField(max_length=400)
    core_sig_choice = models.ManyToManyField(SIGroup,related_name='core_sig_choice')
    core_sig_interests = models.TextField(max_length=400)
    core_sig_projects = models.TextField(max_length=400)
    next_tech = models.TextField(max_length=400)
    aux_sig_choice = models.ManyToManyField(SIGroup,related_name='aux_sig_choice')
    aux_sig_interests = models.TextField(max_length=400)
    picture = models.TextField(max_length=400)
    witty_question = models.TextField(max_length=400)
    timestamp = models.DateTimeField(default=datetime.now())
    qualified_for_round = models.IntegerField(default=1)
    current_round = models.CharField(max_length=30,default='Pending Resume Evaluation')

    def __str__(self):
        return self.name

    def attributes(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value

class ResumeEvaluation(models.Model):

	resume = models.ForeignKey('Resume',related_name='resume')
	name = models.CharField(max_length=50)
	score = models.IntegerField(null=True)
	comments = models.TextField(max_length=200)
	qualified = models.BooleanField(default=False)
	informal_comments = models.TextField(max_length=200)
	evaluated_by = models.ForeignKey(User,related_name='evaluated_by')
	sig_evaluators = models.CharField(max_length=50)
	current_round = models.CharField(max_length=30,default='Pending Resume Evaluation')

	def __str__(self):
		return self.name
