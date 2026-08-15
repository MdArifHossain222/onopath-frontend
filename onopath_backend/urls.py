from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', views.auth_view, name='auth'),
    path('study/', views.study, name='study'),
    path('study/<int:subject_id>/', views.study_chapters, name='study_chapters'),
    path('study/chapter/<int:chapter_id>/read/', views.study_read, name='study_read'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/play/<int:quiz_id>/', views.quiz_play, name='quiz_play'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)