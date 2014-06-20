from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class SIGroup(models.Model):
    """Stores entries for a single SIG."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
	return self.name

class ClubMember(models.Model):
    """Stores details of each club member"""
    userid = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    sig = models.ManyToManyField(SIGroup,related_name="sigs")

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """Stores details of articles"""
    author = models.ForeignKey(ClubMember,related_name="articleAuthor")
    title = models.CharField(max_length = 255)
    text = models.TextField()
    published = models.BooleanField(default=False,editable=False)
    dateTimePublished = models.DateTimeField(blank=True,editable=False)

    def __unicode__(self):
        return self.title

    def publish(self):
        self.publish = True
        dateTimePublished = timezone.localtime(timezone.now())

class Project(models.Model):
    """Stores details of projects"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    sig = models.ForeignKey(SIGroup,related_name="projectSIG")
    projectHead = models.ForeignKey(ClubMember,related_name="projectHead")
    members = models.ManyToManyField(ClubMember,related_name="members")

    def __unicode__(self):
        return self.name
