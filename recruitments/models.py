from django.db import models
from SIG.models import SIGroup
from datetime import datetime

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
	
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	roll_number = models.CharField(max_length=15)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
	phone_number = models.DecimalField(max_digits=10, decimal_places=0)
	email_id = models.EmailField(max_length=254)
	about_me = models.TextField(max_length=200)
	why_ie = models.TextField(max_length=200)
	core_sig_choice = models.ManyToManyField(SIGroup,related_name='core_sig_choice')
	core_sig_interests = models.TextField(max_length=200)
	core_sig_projects = models.TextField(max_length=200)
	aux_sig_choice = models.ManyToManyField(SIGroup,related_name='aux_sig_choice')
	aux_sig_interests = models.TextField(max_length=200)
	timestamp = models.DateTimeField(default=datetime.now())
	score = models.IntegerField(null=True)
	comments = models.TextField(max_length=200)
	informal_comments = models.TextField(max_length=200)
	qualified_for_round = models.IntegerField(default=1)
	qualified = models.BooleanField(default=False)
	evaluated_by = models.CharField(max_length=30)
	current_round = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name
