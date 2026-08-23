from django.contrib import admin
from django.urls import path, include  # include ইম্পোর্ট করা হয়েছে
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # django-browser-reload রুট (সবার উপরে বা সুবিধাজনক স্থানে রাখা ভালো)
    path('__reload__/', include('django_browser_reload.urls')),

    path('', views.home, name='home'),
    path('auth/', views.auth_view, name='auth'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # পাসওয়ার্ড রিসেট রাউটসমূহ (ইমেইল ভিত্তিক)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    # কুইজ সেকশন রাউটসমূহ (লেভেল, সাবজেক্ট, চ্যাপ্টার ও প্লে)
    path('quiz/', views.quiz_classes_view, name='quiz_classes'),
    path('quiz/subjects/<str:level>/', views.quiz_subjects, name='quiz_subjects'),
    path('quiz/chapters/<int:subject_id>/', views.quiz_chapters, name='quiz_chapters'),
    path('quiz/daily/<int:chapter_id>/', views.daily_quiz_play, name='daily_quiz_play'),
    path('quiz/all/<int:chapter_id>/', views.chapter_quiz_play, name='chapter_quiz_play'),
    path('quiz/solve/<int:chapter_id>/', views.chapter_solve_view, name='chapter_solve_view'),
    
    # স্টাডি সেকশন (SSC এবং HSC লেভেল ভিত্তিক)
    path('study/', views.study_classes, name='study'), 
    path('study/', views.study_classes, name='study_classes'),
    path('study/<str:level>/', views.study_subjects, name='study_subjects'), 
    path('study/chapter/<int:subject_id>/', views.study_chapters, name='study_chapters'), 
    path('study/read/<int:chapter_id>/', views.study_read, name='study_read'), 
    path('study/read/json/<int:chapter_id>/', views.study_read_json, name='study_read_json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)