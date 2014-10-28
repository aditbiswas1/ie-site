from django.db import models

# Create your models here.

class Event(models.Model):
    """Details of event"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    contact_name = models.CharField(max_length=100)
    contact_number = models.DecimalField(max_digits=10,decimal_places=0)

    def __unicode__(self):
        return self.name

class Round(models.Model):
    """Details of each round"""
    event = models.ForeignKey(Event)
    round_no = models.IntegerField()
    description = models.TextField()
    venue = models.CharField(max_length=300)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.event.name + str(self.round_no)

class Member(models.Model):
    """Details of each member of the team-Not using for now. :P"""
    name = models.CharField(max_length=100)
    contact_number = models.DecimalField(max_digits=10,decimal_places=0)
    roll_no = models.CharField(max_length=10)

    def __unicode__(self):
        return self.roll_no+ '. '+ self.name

class Registration(models.Model):
    """Details of each team"""
    event = models.ForeignKey(Event)
    members = models.TextField()
    contact_number = models.DecimalField(max_digits=10,decimal_places=0)
    alternate_contact_number = models.DecimalField(max_digits=10,decimal_places=0,null=True) 
    current_round = models.IntegerField(default=1)

    def __unicode__(self):
        string = self.event.name + ' ' + members
        return string
