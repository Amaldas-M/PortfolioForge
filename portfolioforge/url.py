from django.urls import path
from portfolioforge import views

urlpatterns = [
    path('', views.log, name='log_in'),
    path('signup/', views.signup, name='signup'),
    
    path('index/', views.forms, name='home-form'),
    path('home/', views.home, name='home'),
    path('about/', views.details, name='about-form'),
    path('edu/', views.EducationFormView.as_view(), name='education_form'),
    path('exp/', views.ExperienceFormView.as_view(), name='experience_form'),
    path('abou/', views.about, name='about'),
    path('service/', views.ServiceFormView.as_view(), name='service_form'),
    path('servi/', views.service, name='service'),
    path('proj/', views.ProjectFormView.as_view(), name='project_form'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('service-names/', views.service_names, name='service_names'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('download_latest_resume/', views.download_latest_resume, name='download_latest_resume'),

]