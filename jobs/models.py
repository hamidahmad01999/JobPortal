from django.db import models

from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.utils import timezone

class newJob(models.Model):
    JobType=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
        ('Contract', 'Contract'),
    ]
    JobLevel=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    jobTitle=models.CharField(max_length=50, blank=False, null=False, default=None)
    jobDescription=models.CharField(max_length=250,null=False, blank=True)
    skillsRequirement=models.CharField(max_length=250,blank=False, default=None, null=False)
    experienceRequirement=models.CharField(max_length=250,blank=False, default=None, null=True)
    educationRequirement=models.CharField(max_length=250,blank=False, default=None, null=False)
    jobLocation=models.CharField(max_length=100, blank=False, null=False)
    salaryRange=models.IntegerField(blank=True, null=False)
    companyName=models.CharField(max_length=40, blank=True, null=False)
    jobLevel=models.CharField(choices=JobLevel, max_length=40, null=False, blank=False, default="Intermediate")
    jobType=models.CharField(choices=JobType, max_length=40, null=False, blank=False, default="Full Time")
    companyDescription=models.CharField(max_length=250,blank=False, default=None, null=False)
    postJobSlug=AutoSlugField(populate_from="jobTitle", unique=True, null=True, default=None)
    companyImage=models.ImageField(upload_to='company_image/')

def default_resume():
    # Provide the path to the default file you want to use
    return 'media/resume/noorani_qaida.pdf'

class CreateEmployeeModel(models.Model):
    Language_Choices=[
        ('Urdu','Urdu'),
        ("English","English"),
        ('German', 'German'),
        ('Punjabi', 'Punjabi'),
        ('Hindi',"Hindi"),
        ('French', 'French')

    ]
    Work_Experience=[
        ("None", "None"),
        ("6 Month", "6 Month"),
        ("1 Year", "1 Year"),
        ("2-3 years", "2-3 Years"),
        ("3-5 Years", "3-5 Years"),
        ("5-7 Years", "5-7 Years"),
        ("7-10 Years", "7-10 Years"),
        ("10-12 Years", "10-12 Years"),
        ("12-15 Years", "12-15 Years"),
        ("15+ Years", "15+ Years"),
    ]
    employeeName=models.CharField(max_length=50, null=False, blank=False, default=None,)
    employeeEmail=models.EmailField( null=False, blank=False, default=None,)
    employeePhone=models.CharField(max_length=11, blank=False, null=False, default=None)
    employeeCity=models.CharField(max_length=25, blank=False, null=False)
    employeeAddress=models.CharField(max_length=200, blank=False, null=False, default=None)
    employeeProfession=models.CharField(max_length=25, blank=True, null=True)
    employeeSkills=models.CharField(max_length=300, blank=False, null=False, default=None)
    employeeEducation=models.CharField(max_length=200, blank=False, null=False, default=None)
    employeeWorkExperience=models.CharField(max_length=200, blank=False, null=False, default=None)
    employeeWorkExperienceYear=models.CharField(choices=Work_Experience,max_length=15, default="None", blank=False, null=False,)
    employeeLanguages=models.CharField( null=False,blank=False,default="Urdu", max_length=60)
    employeeProfessionalSummary=models.CharField(max_length=300, blank=True, null=False, default=None)
    employeeImage=models.ImageField(upload_to='employeeImages/', default=None)
    employeeFacebook=models.CharField(max_length=150, null=False, blank=True)
    employeeInstagram=models.CharField(max_length=150, null=False, blank=True)
    employeeLinkedIn=models.CharField(max_length=150, null=False, blank=True)
    employeeGithub=models.CharField(max_length=150, null=False, blank=True)
    employeeSlug=AutoSlugField(populate_from='employeeName', unique=True, null=True, default=None)
    employeeResume=models.FileField(upload_to='resume/')
