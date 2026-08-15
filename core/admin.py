from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import StudentProfile, Notice, Subject, Chapter, Lesson

# Profile-কে User-এর ভেতরে ইনলাইন হিসেবে দেখানোর জন্য
class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

# UserAdmin কাস্টমাইজেশন
class UserAdmin(BaseUserAdmin):
    inlines = (StudentProfileInline,)

# ডিফল্ট User unregister করে কাস্টম Inline সহ পুনরায় register
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# শুধু কনটেন্ট সম্পর্কিত মডেলগুলো CORE-এ থাকবে
admin.site.register(Notice)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Lesson)