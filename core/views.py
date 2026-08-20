from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileUpdateForm, UserUpdateForm
from .models import (
    Chapter,
    Notice,
    Option,
    Question,
    StudentProfile,
    Subject,
    UserAnswer,
)


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


# ৬. ডাইনামিক প্রোফাইল ভিউ
@login_required
def profile(request):
    profile_obj, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'avatar' in request.FILES:
            profile_obj.avatar = request.FILES['avatar']
            profile_obj.save()
            messages.success(request, 'প্রোফাইল ছবি সফলভাবে আপডেট হয়েছে!')
            return redirect('profile')

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

    user_answers = UserAnswer.objects.filter(user=request.user).order_by('-id')

    total_quizzes = user_answers.values('question__quiz').distinct().count()
    correct_answers_count = user_answers.filter(is_correct=True).count()
    total_points = correct_answers_count * 10
    chapters_completed = user_answers.filter(is_correct=True).values('question__quiz__chapter').distinct().count()

    recent_activities = []
    seen_chapters = set()
    for ans in user_answers:
        try:
            chapter = ans.question.quiz.chapter
            subject = chapter.subject
            if chapter.id not in seen_chapters:
                seen_chapters.add(chapter.id)
                recent_activities.append({
                    'subject_title': subject.name,
                    'chapter_title': chapter.title,
                    'chapter_id': chapter.id,
                })
        except AttributeError:
            continue
        if len(recent_activities) >= 5:
            break

    context = {
        'profile': profile_obj,
        'u_form': u_form,
        'p_form': p_form,
        'chapters_completed': chapters_completed,
        'quizzes_completed': total_quizzes,
        'total_points': total_points,
        'recent_activities': recent_activities,
    }
    return render(request, 'profile.html', context)


# ৭. আমাদের কথা (About) ভিউ
def about(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'about.html', {'notices': notices})


# ==========================================
# কুইজ সেকশন
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


# ক. অল কুইজ (সকল প্রশ্ন - লগইন বাধ্যতামূলক)
def chapter_quiz_play(request, chapter_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'সকল প্রশ্ন বা অল কুইজ খেলতে অনুগ্রহ করে প্রথমে লগইন করুন অথবা অ্যাকাউন্ট তৈরি করুন!')
        return redirect('auth')

    chapter = get_object_or_404(Chapter, id=chapter_id)
    daily_mcqs = list(Question.objects.filter(quiz__chapter=chapter, question_type='mcq').order_by('id'))
    total_questions_count = len(daily_mcqs)

    submitted_qid = None
    selected_option_id = None
    correct_option_id = None

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        raw_option_id = request.POST.get('option_id')

        if question_id and raw_option_id:
            try:
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=raw_option_id)
                is_correct = selected_option.is_correct

                submitted_qid = int(question_id)
                selected_option_id = int(raw_option_id)

                correct_opt = question.options.filter(is_correct=True).first()
                if correct_opt:
                    correct_option_id = correct_opt.id

                UserAnswer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={
                        'selected_option': selected_option,
                        'is_correct': is_correct
                    }
                )
                messages.success(request, 'আপনার উত্তর সফলভাবে জমা হয়েছে!')
            except (Question.DoesNotExist, Option.DoesNotExist):
                messages.error(request, 'ত্রুটি ঘটেছে, আবার চেষ্টা করুন।')

    context = {
        'chapter': chapter,
        'daily_mcqs': daily_mcqs,
        'daily_solve': None,
        'submitted_qid': submitted_qid,
        'selected_option_id': selected_option_id,
        'correct_option_id': correct_option_id,
        'has_more_questions': False,
        'total_questions_count': total_questions_count,
        'page_title': 'সকল কুইজ (All Quiz)',
    }
    return render(request, 'quiz-play.html', context)


# খ. ডেইলি কুইজ (প্রতিদিন ৫টি প্রশ্ন - লগইন ছাড়া খেলা যাবে)
def daily_quiz_play(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    all_mcqs = list(Question.objects.filter(quiz__chapter=chapter, question_type='mcq').order_by('id'))
    total_questions_count = len(all_mcqs)
    chunk_size = 5  

    if total_questions_count <= chunk_size:
        daily_mcqs = all_mcqs
    else:
        today_seed = date.today().toordinal()
        start_index = (today_seed * chunk_size) % total_questions_count
        end_index = start_index + chunk_size

        if end_index <= total_questions_count:
            daily_mcqs = all_mcqs[start_index:end_index]
        else:
            daily_mcqs = all_mcqs[start_index:] + all_mcqs[:end_index % total_questions_count]

    submitted_qid = None
    selected_option_id = None
    correct_option_id = None

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        raw_option_id = request.POST.get('option_id')

        if question_id and raw_option_id:
            try:
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=raw_option_id)
                is_correct = selected_option.is_correct

                submitted_qid = int(question_id)
                selected_option_id = int(raw_option_id)

                correct_opt = question.options.filter(is_correct=True).first()
                if correct_opt:
                    correct_option_id = correct_opt.id

                if request.user.is_authenticated:
                    user_answers = UserAnswer.objects.filter(user=request.user, question=question)
                    if user_answers.exists():
                        user_answer = user_answers.first()
                        user_answer.selected_option = selected_option
                        user_answer.is_correct = is_correct
                        user_answer.save()
                        user_answers.exclude(pk=user_answer.pk).delete()
                    else:
                        UserAnswer.objects.create(
                            user=request.user,
                            question=question,
                            selected_option=selected_option,
                            is_correct=is_correct
                        )
                    messages.success(request, 'আপনার উত্তর সফলভাবে জমা হয়েছে!')
                else:
                    messages.info(request, 'উত্তর যাচাই করা হয়েছে। আপনার স্কোর সেভ করতে লগইন করুন!')
            except (Question.DoesNotExist, Option.DoesNotExist):
                messages.error(request, 'ত্রুটি ঘটেছে, আবার চেষ্টা করুন।')

    context = {
        'chapter': chapter,
        'daily_mcqs': daily_mcqs,
        'daily_solve': None,
        'submitted_qid': submitted_qid,
        'selected_option_id': selected_option_id,
        'correct_option_id': correct_option_id,
        'has_more_questions': False,
        'total_questions_count': total_questions_count,
        'page_title': 'ডেইলি কুইজ (Daily Quiz)',
    }
    return render(request, 'quiz-play.html', context)


# গ. সলভ কোশ্চেন ভিউ
def chapter_solve_view(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    solve_questions = Question.objects.filter(quiz__chapter=chapter, question_type='solve').order_by('id')

    context = {
        'chapter': chapter,
        'solve_questions': solve_questions,
        'page_title': 'সলভ কোশ্চেন (Solve Questions)',
    }
    return render(request, 'chapter-solve.html', context)


# ==========================================
# স্টাডি সেকশন ভিউসমূহ
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