from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import StudentProfile, Notice, Subject, Chapter, Quiz, Question, Option, UserAnswer
from .forms import UserUpdateForm, ProfileUpdateForm

# ১. হোম ভিউ
def home(request):
    return render(request, 'index.html')

# ২. অথেন্টিকেশন ভিউ
def auth_view(request):
    return render(request, 'auth.html')

# ৩. সাইন-আপ লজিক
def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        username = email.split('@')[0] if email else phone

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'এই ইমেইল বা অ্যাকাউন্টটি আগেই ব্যবহার করা হয়েছে!')
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
        messages.success(request, 'আপনার অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে!')
        return redirect('home')

    return render(request, 'auth.html')

# ৪. লগইন লজিক
def login_view(request):
    # আগের জমে থাকা সব মেসেজ পরিষ্কার করে দেওয়া
    storage = get_messages(request)
    for _ in storage:
        pass

    if request.method == 'POST':
        user_input = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

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
            messages.success(request, 'সফলভাবে লগইন হয়েছে!')
            return redirect('profile')
        else:
            messages.error(request, 'ইমেইল, ফোন নম্বর বা পাসওয়ার্ড ভুল হয়েছে!')
            return render(request, 'auth.html', {'saved_username': user_input})

    return render(request, 'auth.html')

# ৫. লগআউট লজিক
def logout_view(request):
    logout(request)
    messages.info(request, 'আপনি সফলভাবে লগআউট করেছেন।')
    return redirect('home')

# ৬. প্রোফাইল ভিউ
@login_required
def profile(request):
    profile_obj, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_obj)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'আপনার প্রোফাইল সফলভাবে আপডেট করা হয়েছে!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile_obj)

    context = {
        'profile': profile_obj,
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)

# ৭. আমাদের কথা (About) ভিউ
def about(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'about.html', {'notices': notices})


# ==========================================
# কুইজ সেকশন (ডেইলি রোটেশন ও লেভেলভিত্তিক লজিক)
# ==========================================

def quiz_classes_view(request):
    return render(request, 'quiz_classes.html')

def quiz_subjects(request, level):
    level = level.upper()
    if level not in ['SSC', 'HSC']:
        level = 'SSC'
    
    subjects = Subject.objects.filter(level=level)
    context = {
        'subjects': subjects,
        'level': level,
    }
    return render(request, 'quiz-subjects.html', context)

def quiz_chapters(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    chapters = subject.chapters.all().order_by('chapter_number')
    return render(request, 'quiz-chapters.html', {'subject': subject, 'chapters': chapters})

def daily_quiz_play(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    
    today_seed = (date.today() - date(2026, 1, 1)).days
    
    all_mcqs = Question.objects.filter(quiz__chapter=chapter, question_type='mcq').order_by('id')
    all_solves = Question.objects.filter(quiz__chapter=chapter, question_type='solve').order_by('id')
    
    daily_mcqs = []
    daily_solve = None

    if all_mcqs.exists():
        chunk_size = 5
        total_mcqs = all_mcqs.count()
        start_index = (today_seed * chunk_size) % total_mcqs
        end_index = start_index + chunk_size
        
        if end_index <= total_mcqs:
            daily_mcqs = list(all_mcqs[start_index:end_index])
        else:
            daily_mcqs = list(all_mcqs[start_index:]) + list(all_mcqs[:end_index % total_mcqs])

    if all_solves.exists():
        solve_index = today_seed % all_solves.count()
        daily_solve = all_solves[solve_index]

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        raw_option_id = request.POST.get('option_id')
        
        if question_id and raw_option_id:
            try:
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=raw_option_id)
                is_correct = selected_option.is_correct
                
                if request.user.is_authenticated:
                    UserAnswer.objects.create(
                        user=request.user,
                        question=question,
                        selected_option=selected_option,
                        is_correct=is_correct
                    )
                messages.success(request, 'আপনার উত্তর সফলভাবে জমা হয়েছে!')
            except (Question.DoesNotExist, Option.DoesNotExist):
                messages.error(request, 'ত্রুটি ঘটেছে, আবার চেষ্টা করুন।')

    context = {
        'chapter': chapter,
        'daily_mcqs': daily_mcqs,
        'daily_solve': daily_solve,
    }
    return render(request, 'quiz-play.html', context)


# ==========================================
# ১০. স্টাডি সেকশন ভিউসমূহ
# ==========================================
def study_classes(request):
    return render(request, 'study-classes.html')

def study_subjects(request, level):
    level = level.upper()
    if level not in ['SSC', 'HSC']:
        level = 'SSC'
    
    subjects = Subject.objects.filter(level=level)
    context = {
        'subjects': subjects,
        'level': level,
    }
    return render(request, 'study-subject.html', context)

def study_chapters(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    chapters = subject.chapters.all().order_by('chapter_number')
    return render(request, 'study-chapters.html', {'subject': subject, 'chapters': chapters})

def study_read(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    lessons = chapter.lessons.all()
    
    context = {
        'chapter': chapter,
        'lessons': lessons,
    }
    return render(request, 'study-read.html', context)