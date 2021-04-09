from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm as AuthenticationForm, ChangePassword, ModifyDataForm
from music.models import Music
from videos.models import Video

import random

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('main:dash')
    return render(request, 'main/home.html', {})

def loginUser(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('main:dash')
            else:
                messages.error(request, "Invalid Credentials, if you are new please register")
                return redirect('main:login')
        else:
            messages.error(request, "Invalid Credentials, if you are new please register")
            return redirect('main:login')
    return render(request, 'auth/login.html', {'loginForm': form})

def registerUser(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('main:login')
        else:
            messages.error(request, "Registration Error Occured, Please try again")
            return redirect('main:login')
    return render(request, 'auth/register.html', {'registerForm': form})

def search(request):
    query = request.POST.get('query')
    vids = Video.objects.filter(title__contains=query)
    mus = Music.objects.filter(title__contains=query)

    CTX = {'music': mus, 'video': vids}
    if request.user.is_authenticated:
        CTX['user'] = request.user
    return render(request, 'main/searchResults.html', CTX)

@login_required
def dashboard(request):
    vids = Video.objects.all()
    mus = Music.objects.all()
    if len(vids) <= 1:
        n = len(vids)
        if n == 1:
            n = 0
    else:
        n = random.randint(1, len(vids)-1)
    if len(mus) <= 1:
        y = len(mus)
        if y == 1:
            y = 0
    else:
        y = random.randint(1, len(mus)-1)
    return render(request, 'main/dashboard.html', {'user': request.user, 'featured_v': vids[:n+1], 'featured_m': mus[:y+1]})

@login_required
def videos(request):
    return render(request, 'main/dashboard.html', {'user': request.user, 'videos': Video.objects.all()})

@login_required
def music(request):
    return render(request, 'main/dashboard.html', {'user': request.user, 'music': Music.objects.all()})

@login_required
def profile(request):
    form = ModifyDataForm()
    if request.method == "POST":
        form = ModifyDataForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.email = form.data['email']
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.save()
            messages.success(request, "Profile Modification Successful")
            return redirect('main:profile')
        messages.error(request, "Form Validation Error, Please Try Again")
        return redirect('main:profile')
    return render(request, 'main/profile.html', {'user': request.user, 'modifyDataForm': form})

@login_required
def settings(request):
    form = ChangePassword(request.user)
    if request.method == "POST":
        form = ChangePassword(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Change Successful, Login Again with new password.")
            return redirect('main:login')
        messages.error(request, "Form Validation Error, Please Try Again")
        return redirect('main:settings')
    return render(request, 'main/settings.html', {'user': request.user, 'chPasswdForm': form})

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('main:login')


