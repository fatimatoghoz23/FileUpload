from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from pages.form import RegisterUserForm, uploadfile
from pages.models import UploadFile, User

# Create your views here.

def index(request):
      files=UploadFile.objects.all()
    
      if request.method == "POST":
                  form=uploadfile(request.POST,request.FILES)
                  if request.user.is_authenticated and not request.user.is_staff :  

                   if form.is_valid():
                      form.save()
                  else:   
                      return redirect('register')

      return render(request,'index.html',{'forms':uploadfile(),'files':files})

def delete(request,pk):
          file=get_object_or_404(UploadFile,pk=pk)
          file.delete()
          return redirect('index')

def pagelogin(request):
       if request.method == 'POST':
            email= request.POST.get('email')
            password= request.POST.get('password')
            user =authenticate(request, username= email, password= password)  
            if user is not None :
                login(request , user)
                return redirect('index')

            else:
            
                messages.info(request,'Username OR password is incorrect')
                return redirect('login')
       else:
         return render(request,'login.html',{})  

def logoutUser(request):
    logout(request)
    return redirect('login')  

def register(request):
                if request.method == "POST":
                  form=RegisterUserForm(request.POST,request.FILES)
                  if form.is_valid():
                      u= form.save(commit=False)
                      u.username=u.email
                      u.save()
                      
                      messages.info(request,'Your account has be created')
                      return redirect('login')
                  else:
                      messages.warning(request,'somthing went wrong')
                      return redirect('register')
                else:
                  form=RegisterUserForm()
                  return render(request,'register.html',{'form':form})            
