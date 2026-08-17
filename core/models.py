from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # পড়াশোনার অগ্রগতি সংক্রান্ত ফিল্ডসমূহ
    chapters_completed = models.IntegerField(default=0)
    quizzes_completed = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    LEVEL_CHOICES = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='SSC')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.level} - {self.name}"


# ২. অধ্যায় (যেমন: গতি, বল, কাজ-ক্ষমতা-শক্তি)
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"{self.subject.name} - {self.title}"


# ৩. অধ্যায়ের পড়া/নotes
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="লেসনের শিরোনাম")
    content = models.TextField(verbose_name="লেসন কনটেন্ট")

    def __str__(self):
        return f"Lesson: {self.title or self.chapter.title}"


# ৪. কুইজ মডেল (অধ্যায়ভিত্তিক)
class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="কুইজের শিরোনাম/অধ্যায়")
    description = models.TextField(blank=True, verbose_name="বর্ণনা")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chapter.title if self.chapter else ''} - {self.title}"


# ৫. কুইজের প্রশ্ন মডেল (MCQ এবং Solve আলাদা করার জন্য)
class Question(models.Model):
    QUESTION_TYPES = (
        ('mcq', 'এমসিকিউ (MCQ)'),
        ('solve', 'সলভ প্রশ্ন (Solving Question)'),
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="প্রশ্ন")
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='mcq', verbose_name="প্রশ্নের ধরন")
    explanation = models.TextField(blank=True, verbose_name="ব্যাখ্যা / সলভ")
    order_number = models.IntegerField(default=1, verbose_name="লুপ সিরিয়াল নম্বর")

    def __str__(self):
        return f"[{self.get_question_type_display()}] {self.text[:50]}"


# ৬. প্রশ্নের অপশন মডেল
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255, verbose_name="অপশন")
    is_correct = models.BooleanField(default=False, verbose_name="সঠিক উত্তর?")

    def __str__(self):
        status = "সঠিক" if self.is_correct else "ভুল"
        return f"{self.text} ({status})"


# ৭. ইউজারের উত্তর সংরক্ষণের মডেল
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Q.{self.question.id} ({'সঠিক' if self.is_correct else 'ভুল'})"