"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobportal import views
from jobs import createjob_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('createjob/', createjob_views.createJob, name='createjob'),
    path('createjob/postjob', createjob_views.PostJob, name='postjob'),
    path('job/', createjob_views.ShowJobs, name="jobs"),
    path('job/delete/<slug>/', createjob_views.DeleteJob, name="deletejob"),
    path('job/detail/<slug>/', createjob_views.JobDetail, name='jobdetail'),
    path('job/edit/<slug>/', createjob_views.EditJob, name='editjob'),
    path('job/edited/<slug>/', createjob_views.EditedJob, name='editedjob'),
    path('createemployeeprofile/', createjob_views.EmployeeProfile, name="employeeprofile"),
    path("saveemployee/", createjob_views.SaveEmployee, name="saveemployee"),
    path('professionals/', createjob_views.Professionals, name='professionals'),
    path('professionaldetails/<slug>/', createjob_views.ProfessionalDetails, name='profdetail'),
    path('professionals/edit/<slug>/', createjob_views.EditProfessionalDetails, name='profdedit'),
    path('professionals/edited/<slug>/', createjob_views.EditedProfessionalDetails, name='profdedited'),
    path('professionals/delete/<slug>/', createjob_views.DeleteProfessional, name='profdelete'),
]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )