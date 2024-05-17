from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, Mentor, Course, Admin

@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        if request.user.profile.role == 'admin':
            return render(request, 'index.html')
        else:
            return redirect('user_page')
    return redirect('login')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            profile = Profile.objects.get(user=user)
            profile.role = role
            profile.save()
            return redirect('/login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def user_page(request):
    return render(request, 'user_page.html')

@csrf_exempt
def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('courseTitle')
        description = request.POST.get('courseDescription')
        price = request.POST.get('coursePrice')
        Course.objects.create(title=title, description=description, price=price)
    return redirect('/')

@csrf_exempt
def approve_mentor(request, mentor_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        mentor = Mentor.objects.get(id=mentor_id)
        if action == 'approve':
            mentor.approved = True
        else:
            mentor.approved = False
        mentor.save()
    return redirect('/')

@csrf_exempt
def add_admin(request):
    if request.method == 'POST':
        name = request.POST.get('adminName')
        email = request.POST.get('adminEmail')
        Admin.objects.create(name=name, email=email)
    return redirect('/')