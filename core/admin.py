from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import StudentProfile, Notice, Subject, Chapter, Lesson, Quiz, Question, Option, UserAnswer

# Profile-কে User-এর ভেতরে ইনলাইন হিসেবে দেখানোর জন্য
class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

# UserAdmin কাস্টমাইজেশন
class UserAdmin(BaseUserAdmin):
    inlines = (StudentProfileInline,)

# ডিফল্ট User unregister করে কাস্টম Inline সহ পুনরায় register
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# ==========================================
# কুইজ অপশনকে প্রশ্নের ভেতরে দেখানোর জন্য Inline কনফিগারেশন
# ==========================================
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # একসাথে ৪টি অপশনের ঘর দেখাবে

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('id', 'text', 'quiz', 'question_type') # অ্যাডমিন লিস্টে সুন্দর দেখানোর জন্য
    search_fields = ('question_text',)

# ==========================================
# Lesson-এর জন্য কাস্টম অ্যাডমিন ও ফিল্টার কনফিগারেশন
# ==========================================
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter')  # তালিকায় লেসন ও চ্যাপ্টার দেখাবে
    list_filter = ('chapter',)           # ডানপাশে চ্যাপ্টার অনুযায়ী ফিল্টার করার অপশন থাকবে
    search_fields = ('title',)           # সার্চ বক্স থাকবে

# সাধারণ মডেলগুলো রেজিস্টার
admin.site.register(Notice)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Lesson, LessonAdmin)  # Lesson-কে কাস্টম ফিল্টার সহ রেজিস্টার করা হলো
admin.site.register(Quiz)

# Question-কে কাস্টম Admin সহ রেজিস্টার করা হলো (Option আলাদা রেজিস্টার হবে না)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer)