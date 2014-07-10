from django.contrib import admin
from SIG.models import SIGroup,ClubMember,Article,Project
from guardian.shortcuts import get_objects_for_user
class SIGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ArticleAdmin(admin.ModelAdmin):
#Show only those articles the user has access to.
#Auto assigning the author as the clubmember who is saving the article.
#TODO: Remove slug field from the form if not superuser. If SIG head, show all articles related to that sig.
    prepopulated_fields = {"slug": ("title",)}

    def get_form(self,request,obj=None,**kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            #TODO: Filter list, and prepopulate certain fields.
            print "Not superuser"
            self.exclude.append('author')
        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self,request,obj,form,change):
        if not request.user.is_superuser:
            obj.author = request.user.clubmember
        obj.save()

    def get_queryset(self,request):
        print "Queryset called"
        if request.user.is_superuser:
            return super(ArticleAdmin,self).get_queryset(request)
        articles = get_objects_for_user(request.user,'author',klass=Article) 
        return articles
    
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def has_delete_permission(self,request,obj=None):
        print "Called with obj! ", obj
        if not obj:
            return False
        if(request.user.has_perm('project_head',obj)):
            return True
        return False

    def get_queryset(self,request):
        print "Queryset called"
        if request.user.is_superuser:
            return super(ProjectAdmin,self).get_queryset(request)
        projects = get_objects_for_user(request.user,'project_head',klass=Project)|get_objects_for_user(request.user,'collaborator',klass=Project)
        print projects
        return projects

admin.site.register(SIGroup, SIGroupAdmin)
admin.site.register(ClubMember)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Project,ProjectAdmin)
# Register your models here.
