from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .models import Job
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone

def allblogs(request):
    blogs=Blog.objects
    return render(request,'allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blogdetails = get_object_or_404(Blog ,pk=blog_id)
    return render(request,'details.html',{'blog':blogdetails})

@login_required(login_url='/blog/signup') 
def job(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['details']   and request.FILES['image']:
            job=Job()
            job.name=request.POST['name']
            job.Image=request.FILES['image']
            job.details=request.POST['details']
            job.save()
            return redirect('home')
            

        else:
            return render(request,'job.html',{'error': 'please fill all the fields'})

    else:
        return render(request,'job.html')



@login_required(login_url='/blog/signup')   
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body']   and request.FILES['image']:
            blog=Blog()
            blog.Title=request.POST['title']
            blog.Date=timezone.datetime.now()
            blog.Image=request.FILES['image']
            blog.body=request.POST['body']
            
            blog.hunter=request.user
            blog.save()
            return redirect('home')
            

        else:
            return render(request,'create.html',{'error': 'please fill all the fields'})

    else:
        return render(request,'create.html')

def home(request):
    blog=blog.objects
    return render(request,'base.html',{'products':products})


def signup(request):
    
    if request.method=='POST' :
        
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'Username already equiped'})
            except User.DoesNotExist:
                 user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                 auth.login(request,user)

                 return redirect('home')

        else:
             return render(request,'signup.html',{'error':'password doesn\'t matched'})
    
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST' :
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
             return render(request,'login.html',{'error':'Username or password is incorrect'})

    
    else:
        return render(request,'login.html')

@login_required(login_url='/blog/signup')
def logout(request):
    if request.method=='GET' :
            auth.logout(request)
            return redirect('allblogs')
    

