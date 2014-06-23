from django.contrib import admin
from SIG.models import SIGroup,ClubMember,Article,Project


class SIGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(SIGroup, SIGroupAdmin)
admin.site.register(ClubMember)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Project,ProjectAdmin)
# Register your models here.
