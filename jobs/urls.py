from django.urls import path
from . import views

urlpatterns = [
    path('createjob/', views.createJob, name='createjob'),
    path('createjob/postjob', views.PostJob, name='postjob'),
    path('job/', views.ShowJobs, name="jobs"),
    path('job/delete/<slug>/', views.DeleteJob, name="deletejob"),
    path('job/detail/<slug>/', views.JobDetail, name='jobdetail'),
    path('job/edit/<slug>/', views.EditJob, name='editjob'),
    path('job/edited/<slug>/', views.EditedJob, name='editedjob'),
    path('createemployeeprofile/', views.EmployeeProfile, name="employeeprofile"),
    path("saveemployee/", views.SaveEmployee, name="saveemployee"),
    path('professionals/', views.Professionals, name='professionals'),
    path('professionaldetails/<slug>/', views.ProfessionalDetails, name='profdetail'),
    path('professionals/edit/<slug>/', views.EditProfessionalDetails, name='profdedit'),
    path('professionals/edited/<slug>/', views.EditedProfessionalDetails, name='profdedited'),
    path('professionals/delete/<slug>/', views.DeleteProfessional, name='profdelete'),
]
