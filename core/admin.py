from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
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
# ১. Question ও Option এর জন্য ইম্পোর্ট রিসোর্স কনফিগারেশন
# ==========================================
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'text', 'question_type', 'explanation', 'serial_number', 'solution_text')
        export_order = fields

# ==========================================
# কুইজ অপশনকে প্রশ্নের ভেতরে দেখানোর জন্য Inline কনফিগারেশন
# ==========================================
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # একসাথে ৪টি অপশনের ঘর দেখাবে

# ==========================================
# Question-এর জন্য কাস্টম অ্যাডমিন ও বাল্ক ইম্পোর্ট কনফিগারেশন
# ==========================================
@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = QuestionResource  # এক ক্লিকে এক্সেল বা ফাইল ইম্পোর্টের জন্য
    inlines = [OptionInline] # প্রশ্নের নিচে অপশন দেখানোর জন্য
    
    # অ্যাডমিন লিস্টে id-র পাশাপাশি 'serial_number' কলামটি যোগ করা হলো
    list_display = ('id', 'serial_number', 'text_snippet', 'get_subject', 'get_chapter', 'question_type')
    
    # ডানপাশে ফিল্টার করার অপশন
    list_filter = (
        'quiz__chapter__subject',  # সাবজেক্ট অনুযায়ী ফিল্টার (যেমন: ফিজিক্স, কেমিস্ট্রি)
        'quiz__chapter',           # নির্দিষ্ট চ্যাপ্টার অনুযায়ী ফিল্টার
        'question_type',           # প্রশ্নর ধরন (MCQ নাকি Solve Question)
    )
    
    # সার্চ বক্স যোগ করা হলো (serial_number দিয়েও এখন সার্চ করা যাবে)
    search_fields = ('text', 'serial_number', 'quiz__title', 'quiz__chapter__title')

    # ছোট করে প্রশ্নের অংশ দেখানোর জন্য ফাংশন
    def text_snippet(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_snippet.short_description = 'প্রশ্ন'

    # সাবজেক্ট দেখানোর জন্য ফাংশন
    def get_subject(self, obj):
        try:
            return obj.quiz.chapter.subject.name
        except AttributeError:
            return 'N/A'
    get_subject.short_description = 'বিষয়'

    # চ্যাপ্টার দেখানোর জন্য ফাংশন
    def get_chapter(self, obj):
        try:
            return obj.quiz.chapter.title
        except AttributeError:
            return 'N/A'
    get_chapter.short_description = 'অধ্যায়'

# ==========================================
# ২. Lesson-এর জন্য রিসোর্স ও অ্যাডমিন কনফিগারেশন (স্টাডি সেকশন)
# ==========================================
class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'content', 'order')

@admin.register(Lesson)
class LessonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LessonResource
    list_display = ('title', 'chapter', 'order')  # তালিকায় লেসন ও চ্যাপ্টার দেখাবে
    list_filter = ('chapter',)                   # ডানপাশে চ্যাপ্টার অনুযায়ী ফিল্টার করার অপশন থাকবে
    search_fields = ('title', 'content')         # সার্চ বক্স থাকবে

# সাধারণ মডেলগুলো রেজিস্টার
admin.site.register(Notice)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Quiz)
admin.site.register(UserAnswer)