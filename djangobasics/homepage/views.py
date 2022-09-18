from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from .forms import ResumeForm
from .functions import handle_uploaded_file
from .models import ResumeModel
# Create your views here.
def books(request):
    books = ResumeModel.objects.all()
    return render(request,'index.html',{'context':book})
def homepage(request):
    return render(request,'homepage.html')


@login_required(login_url='/login')
def dashboard(request):
    return render(request,'index.html')

# @login_required(login_url='/login')
# def create_post(request):
#     if request.method == "POST":
#         upload_file = request.FILES['document']
#         print(upload_file.name)
#         print(upload_file.size)
#         fs = FileSystemStorage()
#         fs.save(upload_file.name,upload_file) 
#     return render(request,'post.html')

@login_required(login_url="/login")
def upload_file(request):
    if request.method == "POST":
        resumeForm = ResumeForm(request.POST,request.FILES)
        if resumeForm.is_valid():
            handle_uploaded_file(request.FILES['file'])
            resumeModelInstance = resumeForm.save(commit=False)
            resumeModelInstance.save()
            return redirect("/dashboard")
    else:
        resumeForm = ResumeForm()
    return render(request,"post.html",{"form":resumeForm})