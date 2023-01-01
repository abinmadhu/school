from django.shortcuts import render,redirect
from .models import Course
from .forms import RegForm,DetailForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.safestring import mark_safe
# Create your views here.
def index(request):  
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,"Error occured")

    else:
        form=RegForm()
    return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('button_page')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')    
    else:
        return render(request, 'login.html')          

def logout_user(request):
    logout(request)
    return redirect('index')




def detail(request):
    if request.method=='POST':
        form=DetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('detail')
            
    else:        
        form=DetailForm()
    return render(request, 'detail.html',{'form':form})


def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'dropdown.html', {'courses': courses})

def button_page(request):
    return render(request,'button.html')            