from datetime import datetime
from django.db import models

from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Homeform(models.Model):
    name = models.CharField(max_length=30, null=False)
    profession = models.CharField(max_length=30, null=True)  # profession can be null
    description = models.TextField(max_length=200, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Aboutform(models.Model):
    birthday = models.DateField()
    age = models.IntegerField()
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=30)
    degree = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    freelance = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.phone


class EducationGroup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Education Group {self.pk}"

class Education(models.Model):
    group = models.ForeignKey(EducationGroup, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    institution = models.CharField(max_length=255)
    type_of_study = models.CharField(max_length=255)
    area_of_study = models.CharField(max_length=255)
    score = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.institution} - {self.type_of_study}"

class ExperienceGroup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Experience Group {self.pk}"

class Experience(models.Model):
    group = models.ForeignKey(ExperienceGroup, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company} - {self.position}"
    
    
    
    
    
    

class ServiceGroup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Service Group {self.pk}"

class Service(models.Model):
    group = models.ForeignKey(ServiceGroup, related_name='services', on_delete=models.CASCADE, null=True, blank=True)
    service_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # Add this field

    def __str__(self):
        return self.service_name
    
    

class SkillGroup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Skill Group {self.pk}"

class Skill(models.Model):
    group = models.ForeignKey(SkillGroup, related_name='skills', on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.CharField(max_length=255)
    proficiency = models.PositiveIntegerField()  # Field for proficiency as a percentage
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.skill_name} ({self.proficiency}%)"





class ProjectGroup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Project Group {self.pk}"

class Project(models.Model):
    group = models.ForeignKey(ProjectGroup, related_name='projects', on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Add this field

    def __str__(self):
        return self.project_name
    
    
    
    
class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.resume_file.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_new_user = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()