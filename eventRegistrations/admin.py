from django.contrib import admin
from eventRegistrations import models
# Register your models here.

admin.site.register(models.Event)
admin.site.register(models.Round)
admin.site.register(models.Member)
admin.site.register(models.Registration)
