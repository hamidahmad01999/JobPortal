#Name: Hamid Ahmad
#Development Date: June/July 2023


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import newJob  #importing model to create a Job 
from .models import CreateEmployeeModel #importing model to create a profile 
from django.contrib import messages #for showing messages in template page to user
from .job_forms import CreateEmployeeProfile # importing form to create profile
from .job_forms import CreateEmployeeProfileAdd # importing form to create profile
from .job_forms import CreateJob  #importing form to create job
from .job_forms import ProfessionalSearch  #importing form to filter profile on job portal / professionals page
from PIL import Image  #using pillow to upload image
from django.core.paginator import Paginator # using paginator to give pagination to pages
from django.db.models import Q  # importing for filter
from django.utils.html import escape # to filter input from user  


#this function is to show the page where employer can use to post job
def createJob(request):
    try:
        form=CreateJob()
        return render(request, 'create_job/createjob.html', {'form':form})
    except:
        return redirect('/')

#this function will get the file and check whether user is uploading only image and it will not allow user to upload any other file
def is_Image(file):
    try:
        img=Image.open(file)
        img.verify()
        print('image upload')
        return True
    except:
        print('image not upload')
        False


#this function will use to post the job from employer
def PostJob(request):
    # try:
        if request.method == 'POST':
            form=CreateJob(request.POST, request.FILES)
            if form.is_valid():
                jobTitle=form.cleaned_data.get('jobTitle')
                jobDescription=form.cleaned_data.get('jobDescription')
                skillsRequirement=form.cleaned_data.get('skillsRequirement')
                experienceRequirement=form.cleaned_data.get('experienceRequirement')
                educationRequirement=form.cleaned_data.get('educationRequirement')
                jobLocation=form.cleaned_data.get('jobLocation')
                salaryRange=form.cleaned_data.get('salaryRange')
                companyName=form.cleaned_data.get('companyName')
                companyDescription=form.cleaned_data.get('companyDescription')
                jobType=form.cleaned_data.get('jobType')
                jobLevel=form.cleaned_data.get('jobLevel')
                companyImage=form.cleaned_data.get('companyImage')
                print(jobTitle, experienceRequirement)
           
            
                if(jobTitle=="" or jobDescription=="" or skillsRequirement=="" or experienceRequirement== "" or educationRequirement == "" or jobLocation=="" or salaryRange=="" or companyName=="" or companyDescription =="" or companyImage==None):
                    messages.error(request, "Please fill all the fileds.")
                    return redirect('/createjob')
                if(jobTitle==None or jobDescription==None or skillsRequirement==None or experienceRequirement== None or educationRequirement == None or jobLocation==None or salaryRange==None or companyName==None or companyDescription ==None or companyImage==None):
                        messages.error(request, "Please fill all the fileds.")
                        return redirect('/createjob')

                print(companyImage)
                if is_Image(companyImage):
                        print("No problem")
                else:
                    result="Please only upload Image."
                    print(result)
                    messages.error(request, "Only upload valid Image.")
                    return redirect('/createjob') 

                print(jobTitle, companyName, companyDescription, jobDescription, skillsRequirement,educationRequirement,
                experienceRequirement,jobLocation,salaryRange, jobType,jobLevel, companyImage )

                myPostJob=newJob(jobTitle=jobTitle,companyName=companyName, companyDescription=companyDescription, jobDescription=jobDescription, skillsRequirement=skillsRequirement, educationRequirement= educationRequirement,experienceRequirement=experienceRequirement, jobLocation=jobLocation, salaryRange=salaryRange, jobType=jobType, jobLevel=jobLevel, companyImage=companyImage )
                print(myPostJob)
                print("it's going to save")
                myPostJob.save()
                messages.success(request, "Job Posted sucessfully.")
                return redirect("/createjob")
        print(form.errors)
        messages.error(request, "Job not Posted.")
        return redirect("/createjob")
    # except:
    #     print('excep error')
    #     messages.error(request, "Some kind of internal error.")
    #     return redirect("/createjob")

#this function is to show the jobs where user can finds new and old jobs
def ShowJobs(request):
    try:
        get_jobs= newJob.objects.all()
        result_num=get_jobs.count()
        searchMenu=ProfessionalSearch() #get profiles of job seeker(users)
        #it will be use to filter result in professionals
        if request.method=="POST":
            name = request.POST.get('searchProfessionalName')
            address = request.POST.get('searchProfessionalAddress')
            skills = request.POST.get('searchProfessionalSkills')
            print(name, address, skills)
            professionals=newJob.objects.all()
            if name:
                professionals=professionals.filter(Q(jobTitle__icontains=name) )
                
            # if name:    
            #     professionals=professionals.filter(Q(companyName__icontains=name))
                
            if address:
                professionals=professionals.filter(Q(jobLocation__icontains=address))
    
            if skills:
                professionals=professionals.filter(Q(skillsRequirement__icontains=skills))
            
            if(not name and not address and not skills):
                return redirect('/job')
            result_num=professionals.count()
            return render(request, 'create_job/jobs.html', {'jobs':professionals, 'form':searchMenu,'total':result_num })

        paginator=Paginator(get_jobs,2)
        page_number= request.GET.get('page')
        jobs= paginator.get_page(page_number)
        pages=jobs.paginator.num_pages
        return render(request, "create_job/jobs.html", {'total':result_num,"jobs":jobs, 'form':searchMenu,'pages':[n+1 for n in range(pages)] })
    except:
        messages.error(request, "Some kind of internal error.")
        return redirect("/createjob")

#this function can use to delete any existing jobd
def DeleteJob(request, slug):
    try:
        slug=slug
        get_job = newJob.objects.get(postJobSlug=slug)

        if (not get_job):
            messages.error(request, "Job not found.")
            return redirect("/createjob")

        get_job.delete()

        messages.success(request, "Job Deleted sucessfully.")
        return redirect("/createjob")
    except:
        messages.error(request, "Some kind of internal error.")
        return redirect("/createjob")


#this function is use to show the all details realted to job and redirect to showjobdetails page
def JobDetail(request, slug):
    try:
        slug=slug
        get_job= newJob.objects.get(postJobSlug=slug)
        if(get_job):
            return render(request, 'create_job/job_detail.html', {'job':get_job})
        else:
            messages.error(request, "This job does not exist.")
            return redirect("/createjob")
    except:
        messages.error(request, "Some kind of internal error.")
        return redirect("/createjob")

#this function can use to show edit page of job detail of existing job
def EditJob(request, slug):
    try:
        slug=slug
        get_job= newJob.objects.get(postJobSlug=slug)

        if(get_job):
            form=CreateJob(instance=get_job)
            return render(request, 'create_job/editjob.html', {'form':form, "job":get_job})
        else:
            messages.error(request, "Professional details can not be load to edit now!")
            return redirect('/createjob')
    except:
        messages.error(request, "Some kind of internal error.")
        return redirect("/createjob")
    
#this function will be used to edit the job
def EditedJob(request, slug):
    print('1st')
    try:
        slug=slug
        get_job= newJob.objects.get(postJobSlug=slug)
        if(get_job):
            print('2nd')
            if request.method == 'POST':
                print('3rda')
                form=CreateJob(request.POST, request.FILES)
                if form.is_valid():
                    print('3rd')
                    jobTitle=form.cleaned_data.get('jobTitle')
                    jobDescription=form.cleaned_data.get('jobDescription')
                    skillsRequirement=form.cleaned_data.get('skillsRequirement')
                    experienceRequirement=form.cleaned_data.get('experienceRequirement')
                    educationRequirement=form.cleaned_data.get('educationRequirement')
                    jobLocation=form.cleaned_data.get('jobLocation')
                    salaryRange=form.cleaned_data.get('salaryRange')
                    companyName=form.cleaned_data.get('companyName')
                    companyDescription=form.cleaned_data.get('companyDescription')
                    jobType=form.cleaned_data.get('jobType')
                    jobLevel=form.cleaned_data.get('jobLevel')
                    companyImage=form.cleaned_data.get('companyImage')
                    print(jobTitle, experienceRequirement, jobLevel, jobLevel, jobLocation,skillsRequirement,educationRequirement,salaryRange, companyDescription,jobType,jobLevel)
    
    
                    if(jobTitle=="" or jobDescription=="" or skillsRequirement=="" or experienceRequirement== "" or educationRequirement == "" or jobLocation=="" or salaryRange=="" or companyName=="" or companyDescription =="" or companyImage==""):
                        messages.error(request, "Please fill all the fileds.")
                        return redirect(f'/job/edited/{slug}')
                    if(jobTitle==None or jobDescription==None or skillsRequirement==None or experienceRequirement== None or educationRequirement == None or jobLocation==None or salaryRange==None or companyName==None or companyDescription ==None or companyImage==None):
                        messages.error(request, "Please fill all the fileds.")
                        return redirect(f'/job/edited/{slug}')
                    
                    if is_Image(companyImage):
                        print("No problem")
                    else:
                        result="Please only upload Image."
                        print(result)
                        messages.error(request, "Only upload valid Image.")
                        return redirect('/createjob')   
    
                    get_job.jobTitle=jobTitle
                    get_job.jobDescription=jobDescription
                    get_job.skillsRequirement=skillsRequirement
                    get_job.experienceRequirement=experienceRequirement
                    get_job.educationRequirement=educationRequirement
                    get_job.jobLocation=jobLocation
                    get_job.salaryRange=salaryRange
                    get_job.companyName=companyName
                    get_job.companyDescription=companyDescription
                    get_job.jobType=jobType
                    get_job.jobLevel=jobLevel
                    get_job.companyImage=companyImage
                    get_job.save()
    
                    messages.success(request, "Job Updated sucessfully.")
                    return redirect("/job")
        else:
            print(form.errors)
            print('eror')
            messages.error(request, "Job does not exist")
            return redirect("/job")
    except:
        print(form.errors)
        messages.error(request, "Fill all field Or Internal server error.")
        return redirect("/job")
    

# this function will show the that page to user where he can create his profile to get job
def EmployeeProfile(request):
    try:
        SoftSkills=Skills = ["HTML","CSS","JavaScript","Python","Java","C#","PHP","SQL","Node.js","React","Angular","Vue.js","TypeScript","Ruby","Swift","Kotlin","C","C++","R","Shell scripting","Git","Docker","Kubernetes","Amazon Web Services (AWS)","Microsoft Azure","Google Cloud Platform (GCP)","Networking","Cybersecurity","Data Analysis","Machine Learning","Artificial Intelligence","Data Science","Databases","Ruby on Rails","Django","Flask","Spring Framework","Hibernate","Express.js","NestJS","Go (Golang)","Rust","Scala","Haskell","Erlang","Lua","Bash scripting","PowerShell","MongoDB","MySQL","PostgreSQL","Oracle","NoSQL databases","Big Data","Apache Spark","Apache Hadoop","TensorFlow","Keras","PyTorch","scikit-learn","NLTK","OpenCV","Unity","Unreal Engine","Agile Development","DevOps","Continuous Integration (CI)","Continuous Deployment (CD)","Jenkins","Ansible","Puppet","Chef","Terraform","Azure DevOps","GitLab","SonarQube","Kibana","Grafana","Splunk","Bootstrap","Tailwind CSS","Material UI","Android","iOS","React Native","Flutter","Xamarin","Apache Cordova","Adobe PhoneGap","Ionic","Unity for Mobile","NativeScript","Java for Android","Kotlin for Android","Swift for iOS","Objective-C for iOS","C# for Xamarin","JavaScript for Cordova/PhoneGap","TypeScript for Ionic","C# for Unity Mobile","Dart for Flutter","React.js for React Native","Vue.js for NativeScript","Angular for NativeScript","SwiftUI for iOS","Kotlin Multiplatform Mobile (KMM)","Flutter for Web","Progressive Web Apps (PWA)","Ionic with Capacitor","Flutter for Desktop","Flutter for AR/VR","React Native for Windows","Flutter for Linux","Flutter for macOS","Flutter for iOS (macOS host)","Flutter for Android (macOS host)","Flutter for Embedded Devices","Flutter for AI/ML","Flutter for Game Development","Flutter for IoT","Flutter with BLoC pattern","Flutter with Redux","Flutter State Management","Flutter Animation","Flutter Testing","Flutter with Firebase","Flutter with GraphQL","Flutter Maps and Location","Flutter Push Notifications","Cybersecurity","Ethical Hacking","Penetration Testing","Network Security","Web Application Security","Mobile Application Security","Cloud Security","IoT Security","Blockchain Security","Malware Analysis","Incident Response","Digital Forensics","Security Operations Center (SOC)","Threat Intelligence","Other"]
        form=CreateEmployeeProfile()
        form2=CreateEmployeeProfileAdd()
        return render(request, 'employee/createemployee.html', {"form":form, 'form2':form2, 'allskills':SoftSkills})
    except:
        messages.error(request, "Internal server error")
        return redirect('/')


#this function will create the user profile and help him/her to get a better job
def SaveEmployee(request):
    try:
        print("Entered")
        if request.method=="POST":
            print('enter in post')
            form=CreateEmployeeProfile(request.POST, request.FILES)
            if form.is_valid():
                print('form is valid')
                employeeName=form.cleaned_data.get('employeeName')
                employeeEmail=form.cleaned_data['employeeEmail']
                employeePhone=form.cleaned_data['employeePhone']
                employeeAddress=form.cleaned_data['employeeAddress']
                employeeProfession=form.cleaned_data['employeeProfession']
                employeeEducation=form.cleaned_data['employeeEducation']
                employeeCity=form.cleaned_data['employeeCity']
                employeeLanguages=form.cleaned_data['employeeLanguages']
                employeeWorkExperienceYear=form.cleaned_data['employeeWorkExperienceYear']
                employeeWorkExperience=form.cleaned_data['employeeWorkExperience']
                employeeProfessionalSummary=form.cleaned_data['employeeProfessionalSummary']
                employeeImage=request.FILES.get('employeeImage')
                employeeSkills=request.POST.getlist('employeeSkills')
                employeeFacebook=form.cleaned_data['employeeFacebook']
                employeeInstagram=form.cleaned_data['employeeInstagram']
                employeeGithub=form.cleaned_data['employeeGithub']
                employeeLinkedIn=form.cleaned_data['employeeLinkedIn']
                employeeResume=request.FILES.get('file')
                print(employeeName, employeeSkills,employeeResume, employeeImage,employeeFacebook, employeeInstagram,employeeLinkedIn,employeeGithub)
                if is_Image(employeeImage):
                    print("No problem")
                else:
                    result="Please only upload Image."
                    print(result)
                    messages.error(request, "Only upload valid Image.")
                    return redirect('/createemployeeprofile')


                SaveEmployee= CreateEmployeeModel(employeeProfession=employeeProfession,employeeName=employeeName, employeeEmail=employeeEmail, employeePhone=employeePhone, employeeAddress=employeeAddress, employeeSkills=employeeSkills, employeeEducation=employeeEducation, employeeWorkExperience=employeeWorkExperience, employeeProfessionalSummary=employeeProfessionalSummary, employeeImage=employeeImage, employeeCity=employeeCity, employeeLanguages=employeeLanguages,employeeWorkExperienceYear=employeeWorkExperienceYear,employeeFacebook=employeeFacebook,employeeInstagram=employeeInstagram,employeeGithub=employeeGithub,employeeLinkedIn=employeeLinkedIn
                ,employeeResume=employeeResume)
                SaveEmployee.save()
                messages.success(request, "Your profile created successfully.")
                return redirect('/createemployeeprofile')

        print("Failed")
        print(form.errors)
        # form=CreateEmployeeProfile()
        messages.error(request, form.errors)
        return redirect('/createemployeeprofile')
    except:
        print(form.errors)
        messages.error(request, "Internal Server Error.")
        return redirect('/createemployeeprofile')

#this function will get the profiles of all user and then display on professional page
def Professionals(request):
    try:
        searchMenu=ProfessionalSearch() #get profiles of job seeker(users)
        #it will be use to filter result in professionals
        if request.method=="POST":
            name = request.POST.get('searchProfessionalName')
            address = request.POST.get('searchProfessionalAddress')
            skills = request.POST.get('searchProfessionalSkills')
            print(address)
            professionals=CreateEmployeeModel.objects.all()
            if name:
                professionals=professionals.filter(Q(employeeName__icontains=name))
    
            if address:
                professionals=professionals.filter(Q(employeeAddress__icontains=address))
    
            if skills:
                professionals=professionals.filter(Q(employeeSkills__icontains=skills))
            
            if(not name and not address and not skills):
                return redirect('/professionals')
            result_num=professionals.count()
            return render(request, 'employee/professionals.html', {'total':result_num,'data':professionals, 'form':searchMenu })
            
        professionals=CreateEmployeeModel.objects.all()
        result_num=professionals.count()
        if(professionals):
            paginator=Paginator(professionals,8)
            page_number= request.GET.get('page')
            data= paginator.get_page(page_number)
            pages=data.paginator.num_pages
            print(pages)
            return render(request, 'employee/professionals.html', {'total':result_num,'data':data, 'form':searchMenu,
                                                                    'pages':[n+1 for n in range(pages)] })
        # it will be send to page if there will not exist any professional profie
        return render(request, 'employee/professionals.html', {'data':data, 'form':searchMenu})                                                       
    except:
        messages.error(request, "Internal Server Error / No job seeker profile exists.")
        return redirect('/createemployeeprofile')

# this function will show the page which contain all details of job seeker(user)
def ProfessionalDetails(request, slug):
    try:
        slug=slug
        professionals=CreateEmployeeModel.objects.get(employeeSlug=slug)
        if(professionals):
            print(professionals)
            return render(request, 'employee/professional_details.html', {'data':professionals})
        else:
            messages.error(request, "Professional details does not exist")
            return redirect('/professionals')
    except:
        messages.error(request, "Internal Server Error.")
        return redirect('/createemployeeprofile')
    
#it will show edit/update job seeker details page
def EditProfessionalDetails(request,slug):
    try:
        SoftSkills=Skills = ["HTML","CSS","JavaScript","Python","Java","C#","PHP","SQL","Node.js","React","Angular","Vue.js","TypeScript","Ruby","Swift","Kotlin","C","C++","R","Shell scripting","Git","Docker","Kubernetes","Amazon Web Services (AWS)","Microsoft Azure","Google Cloud Platform (GCP)","Networking","Cybersecurity","Data Analysis","Machine Learning","Artificial Intelligence","Data Science","Databases","Ruby on Rails","Django","Flask","Spring Framework","Hibernate","Express.js","NestJS","Go (Golang)","Rust","Scala","Haskell","Erlang","Lua","Bash scripting","PowerShell","MongoDB","MySQL","PostgreSQL","Oracle","NoSQL databases","Big Data","Apache Spark","Apache Hadoop","TensorFlow","Keras","PyTorch","scikit-learn","NLTK","OpenCV","Unity","Unreal Engine","Agile Development","DevOps","Continuous Integration (CI)","Continuous Deployment (CD)","Jenkins","Ansible","Puppet","Chef","Terraform","Azure DevOps","GitLab","SonarQube","Kibana","Grafana","Splunk","Bootstrap","Tailwind CSS","Material UI","Android","iOS","React Native","Flutter","Xamarin","Apache Cordova","Adobe PhoneGap","Ionic","Unity for Mobile","NativeScript","Java for Android","Kotlin for Android","Swift for iOS","Objective-C for iOS","C# for Xamarin","JavaScript for Cordova/PhoneGap","TypeScript for Ionic","C# for Unity Mobile","Dart for Flutter","React.js for React Native","Vue.js for NativeScript","Angular for NativeScript","SwiftUI for iOS","Kotlin Multiplatform Mobile (KMM)","Flutter for Web","Progressive Web Apps (PWA)","Ionic with Capacitor","Flutter for Desktop","Flutter for AR/VR","React Native for Windows","Flutter for Linux","Flutter for macOS","Flutter for iOS (macOS host)","Flutter for Android (macOS host)","Flutter for Embedded Devices","Flutter for AI/ML","Flutter for Game Development","Flutter for IoT","Flutter with BLoC pattern","Flutter with Redux","Flutter State Management","Flutter Animation","Flutter Testing","Flutter with Firebase","Flutter with GraphQL","Flutter Maps and Location","Flutter Push Notifications","Cybersecurity","Ethical Hacking","Penetration Testing","Network Security","Web Application Security","Mobile Application Security","Cloud Security","IoT Security","Blockchain Security","Malware Analysis","Incident Response","Digital Forensics","Security Operations Center (SOC)","Threat Intelligence","Other"]
    

        print("Edit")
        slug=slug
        get_employee=CreateEmployeeModel.objects.get(employeeSlug=slug)
        selected_skills=(get_employee.employeeSkills)
        
        if(get_employee):
            form=CreateEmployeeProfile(instance=get_employee)
            return render(request, 'employee/professional_edit.html', {'form':form, "employee":get_employee,  'selectedskills':selected_skills, 'allskills':SoftSkills})
        else:
            messages.error(request, "Professional details can not be load to edit now!")
            return redirect('/professionals')
    except:
        
        messages.error(request, "Internal Server Error.")
        return redirect('/createemployeeprofile')
    
#it will edit/update job seeker profile
def EditedProfessionalDetails(request,slug):
    try:
        slug=slug
        get_employee=CreateEmployeeModel.objects.get(employeeSlug=slug)
        if(get_employee):
            if request.method=="POST":
                print('enter in post')
                employeeImage=request.FILES.get('employeeImage')
                print(employeeImage)
                if employeeImage==None:
                    messages.error(request, "Please also upload your image.")
                    return redirect(f'/professionals/edit/{slug}/')
                form=CreateEmployeeProfile(request.POST, request.FILES)
                if form.is_valid():
                    print('form is valid')
                    employeeName=form.cleaned_data.get('employeeName')
                    employeeEmail=form.cleaned_data['employeeEmail']
                    employeePhone=form.cleaned_data['employeePhone']
                    employeeAddress=form.cleaned_data['employeeAddress']
                    employeeProfession=form.cleaned_data['employeeProfession']
                    employeeEducation=form.cleaned_data['employeeEducation']
                    employeeCity=form.cleaned_data['employeeCity']
                    employeeLanguages=form.cleaned_data['employeeLanguages']
                    employeeWorkExperienceYear=form.cleaned_data['employeeWorkExperienceYear']
                    employeeWorkExperience=form.cleaned_data['employeeWorkExperience']
                    employeeProfessionalSummary=form.cleaned_data['employeeProfessionalSummary']
                    employeeImage=request.FILES.get('employeeImage')
                    employeeSkills=request.POST.getlist('employeeSkills')
                    employeeFacebook=form.cleaned_data['employeeFacebook']
                    employeeInstagram=form.cleaned_data['employeeInstagram']
                    employeeGithub=form.cleaned_data['employeeGithub']
                    employeeLinkedIn=form.cleaned_data['employeeLinkedIn']
                    print(employeeName, employeeSkills, employeeImage,employeeFacebook,  employeeInstagram,employeeLinkedIn,employeeGithub)
                    if is_Image(employeeImage):
                        print("No problem")
                    else:
                        result="Please only upload Image."
                        print(result)
                        messages.error(request, "Only upload valid Image.")
                        return redirect('/createemployeeprofile')


                    get_employee.employeeName=employeeName
                    get_employee.employeeEmail=employeeEmail
                    get_employee.employeePhone=employeePhone
                    get_employee.employeeAddress=employeeAddress
                    get_employee.employeeProfession=employeeProfession
                    get_employee.employeeSkills=employeeSkills
                    get_employee.employeeEducation=employeeEducation
                    get_employee.employeeCity=employeeCity
                    get_employee.employeeLanguages=employeeLanguages
                    get_employee.employeeWorkExperience=employeeWorkExperience
                    get_employee.employeeWorkExperienceYear=employeeWorkExperienceYear
                    get_employee.employeeProfessionalSummary=employeeProfessionalSummary
                    get_employee.employeeImage=employeeImage
                    get_employee.employeeFacebook=employeeFacebook
                    get_employee.employeeInstagram=employeeInstagram
                    get_employee.employeeGithub=employeeGithub
                    get_employee.employeeLinkedIn=employeeLinkedIn
                    get_employee.save()
                    messages.success(request, "Your profile Updated successfully.")
                    return redirect('/createemployeeprofile/')
        else:
            print(form.errors)
            messages.error(request, "Your profile not Updated.")
            return redirect('/createemployeeprofile/')
    except:
        print(form.errors)
        messages.error(request, "Internal Server Error.")
        return redirect('/createemployeeprofile')

def DeleteProfessional(request, slug):
    try:
        slug=slug
        get_employee=CreateEmployeeModel.objects.get(employeeSlug=slug)
        get_employee.delete()
        messages.success(request, "Your profile deleted successfully.")
        return redirect('/createemployeeprofile/')
    except:
        messages.error(request, "Internal server error.")
        return redirect('/createemployeeprofile/')