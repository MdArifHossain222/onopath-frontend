import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onopath_backend.settings')
django.setup()

from core.models import Quiz, Question, Chapter

target_chapter, _ = Chapter.objects.get_or_create(id=3, defaults={'title': 'পদার্থবিজ্ঞান - বল'})
quiz_instance, _ = Quiz.objects.get_or_create(chapter=target_chapter)

# যে প্রশ্নগুলোতে গাণিতিক সমস্যা রয়েছে সেগুলোকে নিখুঁত ফরম্যাটে আপডেট করার ডাটা
math_fixes = [
    {
        "serial": 28,
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ভরবেগ \(p = mv\)<br>এখানে, \(m = 2 \text{ kg}\), \(v = 5 \text{ ms}^{-1}\)<br>অতএব, \(p = 2 \times 5 = 10 \text{ kg}\cdot\text{ms}^{-1}\)"
    },
    {
        "serial": 41,
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ত্বরণ \(a = \frac{F}{m} = \frac{20}{10} = 2 \text{ ms}^{-2}\)<br>শেষ বেগ \(v = u + at = 0 + (2 \times 3) = 6 \text{ ms}^{-1}\)"
    },
    {
        "serial": 46,
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ভরবেগের সংরক্ষণ সূত্রানুসারে, \(V = -\frac{mv}{M}\)<br>এখানে, বন্দুকের ভর \(M = 2 \text{ kg}\), গুলির ভর \(m = 10 \text{ g} = 0.01 \text{ kg}\), গুলির বেগ \(v = 300 \text{ ms}^{-1}\)<br>তাহলে, \(V = -\frac{0.01 \times 300}{2} = -1.5 \text{ ms}^{-1}\) (ঋণাত্মক চিহ্ন পশ্চাৎ দিক নির্দেশ করে)।"
    },
    {
        "serial": 96,
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ভরবেগের সংরক্ষণ সূত্রানুসারে, \(m_1u_1 - m_2u_2 = (m_1+m_2)v\)<br>\(\implies (5 \times 4) - (3 \times 2) = (5+3)v\)<br>\(\implies 20 - 6 = 8v \implies 8v = 14 \implies v = 1.75 \text{ ms}^{-1}\)"
    },
    {
        "serial": 98,
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>বলের ঘাত \(J = F \times t = 20 \times 0.5 = 10 \text{ Ns}\) বা \(\text{kg}\cdot\text{ms}^{-1}\)"
    }
]

# ডাটাবেজে নির্দিষ্ট সিরিয়ালের ম্যাথগুলোর ব্যাখ্যা আপডেট করা
updated_count = 0
for item in math_fixes:
    try:
        q = Question.objects.get(quiz=quiz_instance, serial_number=item["serial"])
        q.explanation = item["explanation"]
        q.save()
        updated_count += 1
    except Question.DoesNotExist:
        pass

print(f"✅ সফলভাবে {updated_count}টি গাণিতিক প্রশ্নের ব্যাখ্যা একদম নিখুঁত \( ... \) ফরম্যাটে আপডেট করা হয়েছে!")