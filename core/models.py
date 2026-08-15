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


# ১. বিষয় (যেমন: পদার্থবিজ্ঞান, রসায়ন)
class Subject(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default="📚")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# ২. অধ্যায় (যেমন: গতি, বল, কাজ-ক্ষমতা-শক্তি)
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"{self.subject.name} - {self.title}"


# ৩. অধ্যায়ের পড়া/নotes (একই অধ্যায়ে একাধিক লেসন বা টপিকের জন্য ForeignKey ও title ব্যবহার করা হয়েছে)
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="লেসনের শিরোনাম")
    content = models.TextField(verbose_name="লেসন কনটেন্ট")

    def __str__(self):
        return f"Lesson: {self.title or self.chapter.title}"


# ৪. কুইজ মডেল
class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="কুইজের শিরোনাম")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
    description = models.TextField(blank=True, verbose_name="বর্ণনা")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ৫. কুইজের প্রশ্ন মডেল
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="প্রশ্ন")
    explanation = models.TextField(blank=True, verbose_name="ব্যাখ্যা")

    def __str__(self):
        return self.text[:50]


# ৬. প্রশ্নের অপশন মডেল
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255, verbose_name="অপশন")
    is_correct = models.BooleanField(default=False, verbose_name="সঠিক উত্তর?")

    def __str__(self):
        status = "সঠিক" if self.is_correct else "ভুল"
        return f"{self.text} ({status})"