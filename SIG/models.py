from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from guardian.shortcuts import assign_perm, remove_perm
from django.db.models.signals import m2m_changed
from tinymce import models as tinymce_models

# Create your models here.
class SIGroup(models.Model):
    """Stores entries for a single SIG."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        permissions = (
                ('edit_sig_content','To edit SIG page content'),
                ('view_sig_content','To view SIG internal content'),
            )

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

def sig_changed(sender, **kwargs):
    """To automatically add permissions on adding new sig and remove on removing sig"""
    print kwargs
    if kwargs['action'] is 'pre_clear':
        user = kwargs['instance'].userid
        for removedsig in kwargs['instance'].sig.all():
            remove_perm('view_sig_content',user,removedsig)
            print removedsig, "permission revoked"
    if kwargs['action'] is 'post_add':
        user = kwargs['instance'].userid
        for newsig in kwargs['instance'].sig.all():
            assign_perm('view_sig_content',user,newsig)
            print newsig, "permission added"

    if kwargs['action'] is 'pre_remove':
        user = kwargs['instance'].userid
        for sig_id in kwargs['pk_set']:
            removedsig = SIGroup.objects.get(pk=sig_id)
            print removedsig
            if user.has_perm('view_sig_content',newsig):
                remove_perm('view_sig_content',user,removedsig)
    pass

m2m_changed.connect(sig_changed, sender=ClubMember.sig.through)

class Article(models.Model):
    """Stores details of articles"""
    author = models.ForeignKey(ClubMember,related_name="articleAuthor")
    title = models.CharField(max_length = 255)
    text = tinymce_models.HTMLField()
    sig = models.ForeignKey(SIGroup,related_name="articleSIG")
    published = models.BooleanField(default=False,editable=False)
    dateTimePublished = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

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
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
