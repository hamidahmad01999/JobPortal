from django.contrib import admin
from .models import newJob
from .models import CreateEmployeeModel


class postJob_Admin(admin.ModelAdmin):
    list_display=("jobTitle", "jobDescription", "experienceRequirement", "educationRequirement", "skillsRequirement", "salaryRange", "jobLocation", "companyName", "companyDescription","companyImage")

class CreateEmployeeModel_Admin(admin.ModelAdmin):
    list_display=('employeeName', 'employeeEmail','employeePhone', 'employeeCity','employeeAddress', 'employeeProfession',   'employeeSkills','employeeEducation','employeeWorkExperienceYear',  'employeeWorkExperience','employeeLanguages','employeeProfessionalSummary','employeeImage')

admin.site.register(newJob,postJob_Admin)
admin.site.register(CreateEmployeeModel,CreateEmployeeModel_Admin)

# Register your models here.
