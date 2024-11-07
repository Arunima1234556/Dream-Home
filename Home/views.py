from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Register

# Create your views here.
def index(request):
    return render(request, "index.html")

def base(request):
    return render(request,"base.html")

# <!def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user after successful registration
#             return redirect('Home')  # Redirect to the homepage or another page
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import RegisterForm  # Import the form from forms.py


def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Register.objects.filter(username=username,password=password).first()
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('signin')
        else:
            request.session['username']=username
            return redirect('index')
    return render(request,'signin.html')

def login(request):
    return render(request,'signin.html')


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password=request.POST.get('password')
        
        myreg=Register(name=name, phone=phone, email=email, username=username,password=password)
        myreg.save()
        return redirect('signin')
    return render(request,"register.html")


def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")