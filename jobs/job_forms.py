from django import forms
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator
from .models import CreateEmployeeModel
from .models import newJob
from django.forms import ModelForm

class CreateJob(ModelForm):
    class Meta:
        model=newJob    
        fields=['jobTitle','companyName', 'companyDescription', 'jobDescription', 'skillsRequirement', 'educationRequirement','experienceRequirement',  'salaryRange', 'jobType', 'jobLevel', 'jobLocation','companyImage']

        widgets={
            'jobTitle':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter Job Title here!'}),
            'companyName':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter Company Name here!'}),
            'companyDescription':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter Company description here!'}),
            'jobDescription':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter Company description here!'}),
            'skillsRequirement':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter Skills Requirement here!'}),
            'educationRequirement':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter Education Requirement here!'}),
            'experienceRequirement':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter Experience Requirement here!'}),
            'jobLocation':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter Job Location here!'}),
            'salaryRange':forms.NumberInput(attrs={'class':'form-control',  'placeholder':'Enter Salary Range here!'}),
            'jobType':forms.Select(attrs={'class':'form-control'}),
            'jobLevel':forms.Select(attrs={'class':'form-control'}),
            'companyImage':forms.FileInput(attrs={'class':'form-control'}),
        }
        labels={
            'jobTitle':"Job Title",
            'companyName':'Company Name',
            'companyDescription':'Company Description',
            'jobDescription':'Job Description',
            'skillsRequirement':'Skills Requirement',
            'educationRequirement':'Education Requirement',
            'experienceRequirement':'Experience Requirement',
            'jobLocation':'Job Location',
            'salaryRange':'Salary Range',
            'jobType':'Job Type',
            'jobLevel':'Job Level',
            'companyImage':'Company Image',

        }

class CreateEmployeeProfile(ModelForm):
    class Meta:
        model=CreateEmployeeModel
        fields=['employeeName', 'employeeEmail','employeePhone', 'employeeCity','employeeAddress', 'employeeProfession',
                #    'employeeSkills',
                   'employeeEducation','employeeWorkExperienceYear',  'employeeWorkExperience','employeeLanguages','employeeProfessionalSummary','employeeFacebook','employeeInstagram','employeeLinkedIn','employeeGithub','employeeImage']
    
        widgets={
            'employeeName':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter your name here!', 'max_length':50, 'min_length':3}),
            'employeeEmail':forms.EmailInput(attrs={'class':'form-control',    'placeholder':'Enter your Email here!'}),
            'employeePhone':forms.NumberInput(attrs={'class':'form-control',   'placeholder':'Enter your Phone Number here!'}),
            'employeeCity':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter your City here!'}),
            'employeeAddress':forms.Textarea(attrs={'class':'form-control',    'placeholder':'Enter your Address here!'}),
            'employeeProfession':forms.TextInput(attrs={'class':'form-control',    'placeholder':'Enter your Profession here!'}),
            # 'employeeSkills':forms.Textarea(attrs={'class':'form-control',     'placeholder':'Enter your Skills here!'}),
            'employeeEducation':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Enter your Education here!'}),
            'employeeWorkExperienceYear':forms.Select(attrs={'class':'form-control'}),
            'employeeWorkExperience':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter you work experience in brief.'}),
            'employeeLanguages':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter languages you can speak.'}),
            'employeeProfessionalSummary':forms.Textarea(attrs={'class':'form-control', 'placholder':'Write Your professional Summary.'}),
            'employeeFacebook':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the link of your facebook Profile.'}),
            'employeeInstagram':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the link of your facebook Profile.'}),
            'employeeGithub':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the link of your facebook Profile.'}),
            'employeeLinkedIn':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the link of your facebook Profile.'}),
            'employeeImage':forms.FileInput(attrs={'class':'form-control'})
        }
    
        labels={
            'employeeName':'Name:',
            'employeeEmail':'Email:',
            'employeePhone':'Phone No:',
            'employeeCity':'Your City/Town:',
            'employeeAddress':'Address:',
            'employeeProfession':'Your Profession:',
            # 'employeeSkills':'Skills:',
            'employeeEducation':'Educations:',
            'employeeWorkExperienceYear':'Experience Duration:',   
            'employeeWorkExperience':'Work Experience:',
            'employeeLanguages':'Languages:',
            'employeeProfessionalSummary':'Professional Summary',
            'employeeFacebook':'Your Facebook Profile Link(optional):',
            'employeeInstagram':'Your Instagram Profile Link(optional):',
            'employeeLinkedIn':'Your LinkedIn Profile Link(optional):',
            'employeeGithub':'Your Github Profile Link(optional):',
            'employeeImage':'Image Upload'
        }
    
class CreateEmployeeProfileAdd(forms.Form):
    Your_Skills=[
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('JS','JS')
    ]
    your_skills=forms.MultipleChoiceField(label="Select your languages:", required=True, choices=Your_Skills, widget=forms.CheckboxSelectMultiple(attrs={"class":"form-check-input languages"}))
    

class  ProfessionalSearch(forms.Form):
    searchProfessionalName=forms.CharField(label="Name",max_length=20, required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Search by Name!"}))
    searchProfessionalAddress=forms.CharField(label="Address",max_length=20, required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Search by City/Town!"}))
    searchProfessionalSkills=forms.CharField(label="Skills",max_length=30, required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Search by Skills!"}))
  