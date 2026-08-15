from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StudentProfile

def home(request):
    return render(request, 'index.html')

def auth_view(request):
    return render(request, 'auth.html')

# ১. সাইন-আপ লজিক
def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        username = email.split('@')[0] if email else phone

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'এই ইমেইল বা অ্যাকাউন্টটি আগেই ব্যবহার করা হয়েছে!')
            return render(request, 'auth.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        if full_name:
            name_parts = full_name.split(' ', 1)
            user.first_name = name_parts[0]
            if len(name_parts) > 1:
                user.last_name = name_parts[1]
            user.save()

        StudentProfile.objects.create(user=user, phone_number=phone)
        login(request, user)
        messages.success(request, 'আপনার অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে!')
        return redirect('home')

    return render(request, 'auth.html')

# ২. লগইন লজিক
def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_input, password=password)

        if user is None and '@' in user_input:
            try:
                user_obj = User.objects.get(email=user_input)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is None:
            try:
                profile = StudentProfile.objects.get(phone_number=user_input)
                user = authenticate(request, username=profile.user.username, password=password)
            except StudentProfile.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, 'সফলভাবে লগইন হয়েছে!')
            return redirect('home')
        else:
            messages.error(request, 'ইমেইল, ফোন নম্বর বা পাসওয়ার্ড ভুল হয়েছে!')
            return render(request, 'auth.html')

    return render(request, 'auth.html')

# ৩. লগআউট লজিক
def logout_view(request):
    logout(request)
    messages.info(request, 'আপনি সফলভাবে লগআউট করেছেন।')
    return redirect('home')

# ৪. অন্যান্য পেজের ভিউ
def study(request):
    return render(request, 'study.html')

def quiz(request):
    return render(request, 'quiz.html')

def about(request):
    return render(request, 'about.html')
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')