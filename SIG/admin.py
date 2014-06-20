from django.contrib import admin
from SIG.models import SIGroup


class SIGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(SIGroup, SIGroupAdmin)
# Register your models here.
