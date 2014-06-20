from django.contrib import admin
from SIG.models import SIGroup,ClubMember,Article,Project


class SIGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(SIGroup, SIGroupAdmin)
admin.site.register(ClubMember)
admin.site.register(Article)
admin.site.register(Project)
# Register your models here.
