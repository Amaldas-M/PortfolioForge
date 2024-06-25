from django.contrib import admin
from portfolioforge.models import Aboutform, Education, EducationGroup, Experience, ExperienceGroup, Homeform, Project, ProjectGroup, Resume, Service, ServiceGroup, Skill, SkillGroup

class HomeformAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'description', 'image']

admin.site.register(Homeform, HomeformAdmin)

class AboutformAdmin(admin.ModelAdmin):
    list_display = ['birthday', 'age', 'website', 'email', 'degree', 'phone', 'city', 'freelance']

admin.site.register(Aboutform, AboutformAdmin)

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class EducationGroupAdmin(admin.ModelAdmin):
    inlines = [EducationInline]

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class ExperienceGroupAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline]

admin.site.register(EducationGroup, EducationGroupAdmin)
admin.site.register(ExperienceGroup, ExperienceGroupAdmin)  



class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ServiceGroupAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(ServiceGroup, ServiceGroupAdmin)

    

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class SkillGroupAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

admin.site.register(SkillGroup, SkillGroupAdmin)





class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class ProjectGroupAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]

admin.site.register(ProjectGroup, ProjectGroupAdmin)



admin.site.register(Resume)
