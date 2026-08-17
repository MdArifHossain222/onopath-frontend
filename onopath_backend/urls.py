from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', views.auth_view, name='auth'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # কুইজ সেকশন রাউটসমূহ (লেভেল, সাবজেক্ট, চ্যাপ্টার ও ডেইলি লুপ প্লে)
    path('quiz/', views.quiz_classes_view, name='quiz_classes'),
    path('quiz/subjects/<str:level>/', views.quiz_subjects, name='quiz_subjects'),
    path('quiz/chapters/<int:subject_id>/', views.quiz_chapters, name='quiz_chapters'),
    path('quiz/daily/<int:chapter_id>/', views.daily_quiz_play, name='daily_quiz_play'),
    
    # স্টাডি সেকশন (SSC এবং HSC লেভেল ভিত্তিক)
    path('study/', views.study_classes, name='study'), 
    path('study/<str:level>/', views.study_subjects, name='study_subjects'), 
    path('study/chapter/<int:subject_id>/', views.study_chapters, name='study_chapters'), 
    path('study/read/<int:chapter_id>/', views.study_read, name='study_read'), 
    path('study/', views.study_classes, name='study_classes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)