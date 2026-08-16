from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            messages.success(request, 'সফলভাবে লগইন হয়েছে!')
            return redirect('profile')
        else:
            messages.error(request, 'ইমেইল, ফোন নম্বর বা পাসওয়ার্ড ভুল হয়েছে!')
            return render(request, 'auth.html')

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

# ৮. কুইজ পেজ (তালিকা) ভিউ
def quiz(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz.html', {'quizzes': quizzes})

# ৯. কুইজ খেলা / প্লে ভিউ (সাবমিট এবং ব্যাখ্যা দেখানোর লজিকসহ)
def quiz_play(request, quiz_id=None):
    if not request.user.is_authenticated:
        guest_quiz_count = request.session.get('guest_quiz_count', 0)
        if guest_quiz_count >= 5:
            messages.warning(request, 'আপনার ৫টি ফ্রি কুইজ সম্পন্ন হয়েছে। আরও কুইজ খেলতে অনুগ্রহ করে লগইন করুন।')
            return redirect('auth_view')
        request.session['guest_quiz_count'] = guest_quiz_count + 1

    if quiz_id:
        quiz_obj = get_object_or_404(Quiz, id=quiz_id)
    else:
        quiz_obj = Quiz.objects.first()

    question = quiz_obj.questions.first() if quiz_obj else None
    is_submitted = False
    selected_option_id = None
    correct_option_id = None

    if request.method == 'POST' and question:
        is_submitted = True
        raw_option_id = request.POST.get('option_id')
        
        if raw_option_id:
            try:
                selected_option_id = int(raw_option_id)  # ইন্টিজারে রূপান্তর করা হলো
                selected_option = Option.objects.get(id=selected_option_id)
                is_correct = selected_option.is_correct
                
                # যদি ইউজার লগইন করা থাকে, তার উত্তর ডাটাবেজে সেভ করা যাবে
                if request.user.is_authenticated:
                    UserAnswer.objects.create(
                        user=request.user,
                        quiz=quiz_obj,
                        question=question,
                        selected_option=selected_option,
                        is_correct=is_correct
                    )
            except (Option.DoesNotExist, ValueError):
                pass

    # সঠিক অপশনটি খুঁজে বের করা (ব্যাখ্যা দেখানোর সময় সঠিক উত্তর মার্ক করার জন্য)
    if question:
        correct_opt = question.options.filter(is_correct=True).first()
        if correct_opt:
            correct_option_id = correct_opt.id

    context = {
        'quiz': quiz_obj,
        'question': question,
        'is_submitted': is_submitted,
        'selected_option_id': selected_option_id,
        'correct_option_id': correct_option_id,
    }
    return render(request, 'quiz-play.html', context)

# ১০. স্টাডি সেকশন ভিউসমূহ
def study(request):
    subjects = Subject.objects.all()
    return render(request, 'study.html', {'subjects': subjects})

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