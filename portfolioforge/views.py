from django.http import FileResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from portfolioforge.models import Aboutform, Education, Experience, Homeform

from django.shortcuts import render, redirect
from .models import EducationGroup, ExperienceGroup, Homeform, Project, ProjectGroup, Resume, Service, ServiceGroup, Skill, SkillGroup

from django.shortcuts import render, redirect
from .models import Homeform
from django.db import IntegrityError

from django.shortcuts import render, redirect
from .models import Homeform
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def forms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        description = request.POST.get('describe')
        image = request.FILES.get('image') if request.FILES.get('image') else None

        if name and description:  # Ensuring required fields are present
            try:
                obj1 = Homeform(
                    name=name,
                    profession=profession,  # profession can be None
                    description=description,
                    image=image
                )
                obj1.save()
                return redirect('about-form')
            except IntegrityError as e:
                # Handle database errors
                return render(request, 'home_form.html', {'error': str(e)})
        else:
            # Handle missing required fields
            return render(request, 'home_form.html', {'error': 'Please fill in all required fields.'})

    return render(request, 'home_form.html')



def home(request):
    profile = Homeform.objects.latest('created_at')
    return render(request, 'home.html', {'profile': profile})

def details(request):
    if request.method == 'POST':
        obj2 = Aboutform(
            birthday=request.POST.get('bday'),
            age=request.POST.get('age'),
            website=request.POST.get('website'),
            email=request.POST.get('email'),
            degree=request.POST.get('degree'),
            phone=request.POST.get('phno'),
            city=request.POST.get('place'),
            freelance=(request.POST.get('freelance') == 'yes')
        )
        obj2.save()
        return redirect('education_form')  # Redirect to the education form page

    return render(request, 'about_form.html')

class EducationFormView(View):
    def get(self, request):
        return render(request, 'education.html')

    def post(self, request):
        institutions = request.POST.getlist('institution[]')
        types_of_study = request.POST.getlist('type_of_study[]')
        areas_of_study = request.POST.getlist('area_of_study[]')
        scores = request.POST.getlist('score[]')
        start_dates = request.POST.getlist('start_date[]')
        end_dates = request.POST.getlist('end_date[]')

        education_group = EducationGroup.objects.create()

        for i in range(len(institutions)):
            Education.objects.create(
                group=education_group,
                institution=institutions[i],
                type_of_study=types_of_study[i],
                area_of_study=areas_of_study[i],
                score=scores[i],
                start_date=start_dates[i],
                end_date=end_dates[i]
            )
        return redirect('experience_form')  # Redirect to the experience form page

class ExperienceFormView(View):
    def get(self, request):
        return render(request, 'experience.html')

    def post(self, request):
        companies = request.POST.getlist('company[]')
        positions = request.POST.getlist('position[]')
        locations = request.POST.getlist('location[]')
        start_dates = request.POST.getlist('start_date[]')
        end_dates = request.POST.getlist('end_date[]')

        experience_group = ExperienceGroup.objects.create()

        for i in range(len(companies)):
            Experience.objects.create(
                group=experience_group,
                company=companies[i],
                position=positions[i],
                location=locations[i],
                start_date=start_dates[i],
                end_date=end_dates[i]
            )
        return redirect('service_form')  

def about(request):
    profile = Homeform.objects.latest('created_at')
    about_info = Aboutform.objects.latest('created_at')
    
    try:
        latest_education_group = EducationGroup.objects.latest('created_at')
        education_list = latest_education_group.educations.all()
    except EducationGroup.DoesNotExist:
        education_list = []
    
    try:
        latest_experience_group = ExperienceGroup.objects.latest('created_at')
        experience_list = latest_experience_group.experiences.all()
    except ExperienceGroup.DoesNotExist:
        experience_list = []
    
    context = {
        'profile': profile,
        'about_info': about_info,
        'education_list': education_list,
        'experience_list': experience_list,
    }

    return render(request, 'about.html', context)





class ServiceFormView(View):
    def get(self, request):
        return render(request, 'service_form.html')

    def post(self, request):
        service_names = request.POST.getlist('service[]')
        skill_names = request.POST.getlist('skill[]')
        proficiencies = request.POST.getlist('proficiency[]')

        service_group = ServiceGroup.objects.create()
        skill_group = SkillGroup.objects.create()

        for service_name in service_names:
            Service.objects.create(
                group=service_group,
                service_name=service_name
            )

        for i in range(len(skill_names)):
            Skill.objects.create(
                group=skill_group,
                skill_name=skill_names[i],
                proficiency=proficiencies[i]
            )

        return redirect('project_form')     
    
    
    
    
def service(request):
    try:
        service_name = Service.objects.latest('created_at')
    except Service.DoesNotExist:
        service_name = None

    try:
        latest_service_group = ServiceGroup.objects.latest('created_at')
        service_list = latest_service_group.services.all()
    except ServiceGroup.DoesNotExist:
        service_list = []

    try:
        latest_skill_group = SkillGroup.objects.latest('created_at')
        skill_list = latest_skill_group.skills.all()
    except SkillGroup.DoesNotExist:
        skill_list = []

    context = {
        'service_name': service_name,
        'service_list': service_list,
        'skill_list': skill_list,
    }

    return render(request, 'service.html', context)




    
class ProjectFormView(View):
    def get(self, request):
        return render(request, 'project_form.html')

    def post(self, request):
        project_names = request.POST.getlist('p_name[]')
        descriptions = request.POST.getlist('p_desc[]')

        if project_names and descriptions:
            project_group = ProjectGroup.objects.create()

            for project_name, description in zip(project_names, descriptions):
                Project.objects.create(
                    group=project_group,
                    project_name=project_name,
                    description=description
                )

            return redirect('upload_resume')  

        return render(request, 'project_form.html') 





def project(request):
    try:
        project_name = Project.objects.latest('created_at')
    except Project.DoesNotExist:
        project_name = None

    try:
        latest_project_group = ProjectGroup.objects.latest('created_at')
        project_list = latest_project_group.projects.all()
    except ProjectGroup.DoesNotExist:
        project_list = []


    context = {
        'project_name': project_name,
        'project_list': project_list,
    }

    return render(request, 'project.html', context)



def contact(request):
    profile = Aboutform.objects.latest('created_at')
    return render(request, 'contact.html', {'profile': profile})

def service_names(request):
    try:
        latest_service_group = ServiceGroup.objects.latest('created_at')
        services = latest_service_group.services.order_by('-created_at').values_list('service_name', flat=True)
    except ServiceGroup.DoesNotExist:
        services = []

    return JsonResponse(list(services), safe=False)

def upload_resume(request):
    if request.method == 'POST' and request.FILES['resume']:
        resume_file = request.FILES['resume']
        resume = Resume(resume_file=resume_file)
        resume.save()
        return redirect('home')  
    
    return render(request, 'resume.html')


def download_latest_resume(request):
    latest_resume = Resume.objects.latest('id')
    return FileResponse(latest_resume.resume_file.open(), as_attachment=True, filename=latest_resume.resume_file.name)


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile') and user.profile.is_new_user:
                user.profile.is_new_user = False
                user.profile.save()
                return redirect('home-form')
            return redirect('home')
        else:
            return redirect('signup')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.profile.is_new_user = True
        user.save()
        return redirect('log_in')
    return render(request, 'signup.html')