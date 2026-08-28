import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onopath_backend.settings')
django.setup()

from core.models import Quiz, Question, Option, Chapter

# Physics Chapter 1 (ভৌত রাশি এবং পরিমাপ) - Chapter ID: 2
target_chapter = Chapter.objects.get(id=2) 
quiz_instance = Quiz.objects.get(chapter=target_chapter)

mcq_data_part4_physics_ch1 = [
    {
        "serial": 46,
        "text": "একটি বস্তুর ভর 50 kg এবং আয়তন \\(2 \\text{ m}^3\\) হলে, এর ঘনত্ব কত?",
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ঘনত্ব \\(\\rho = \\frac{\\text{ভর}}{\\text{আয়তন}} = \\frac{50}{2} = 25 \\text{ kg/m}^3\\)।",
        "options": [
            {"text": "ক) 25 kg/m³", "is_correct": True},
            {"text": "খ) 100 kg/m³", "is_correct": False},
            {"text": "গ) 50 kg/m³", "is_correct": False},
            {"text": "ঘ) 12.5 kg/m³", "is_correct": False}
        ]
    },
    {
        "serial": 47,
        "text": "বিশুদ্ধ পানির ঘনত্ব কত?",
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>\\(4^\\circ\\text{C}\\) তাপমাত্রায় বিশুদ্ধ পানির সর্বোচ্চ ঘনত্ব \\(1000 \\text{ kg/m}^3\\) (বা \\(1 \\text{ g/cm}^3\\))।",
        "options": [
            {"text": "ক) 100 kg/m³", "is_correct": False},
            {"text": "খ) 1000 kg/m³", "is_correct": True},
            {"text": "গ) 10 kg/m³", "is_correct": False},
            {"text": "ঘ) 980 kg/m³", "is_correct": False}
        ]
    },
    {
        "serial": 48,
        "text": "কোনো গোলকের ব্যাসার্ধ r হলে এর আয়তন V নির্ণয়ের সঠিক সূত্র কোনটি?",
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>গোলকের আয়তনের সূত্র হলো \\(V = \\frac{4}{3}\\pi r^3\\)।",
        "options": [
            {"text": "ক) \\(V = 4\\pi r^2\\)", "is_correct": False},
            {"text": "খ) \\(V = \\frac{1}{3}\\pi r^3\\)", "is_correct": False},
            {"text": "গ) \\(V = \\frac{4}{3}\\pi r^3\\)", "is_correct": True},
            {"text": "ঘ) \\(V = 2\\pi r^3\\)", "is_correct": False}
        ]
    },
    {
        "serial": 49,
        "text": "একটি সিলিন্ডারের ব্যাসার্ধ r এবং উচ্চতা h হলে, এর আয়তনের সূত্র কোনটি?",
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>সিলিন্ডারের আয়তন = ভূমির ক্ষেত্রফল × উচ্চতা = \\(\\pi r^2 h\\)।",
        "options": [
            {"text": "ক) \\(2\\pi rh\\)", "is_correct": False},
            {"text": "খ) \\(\\frac{1}{3}\\pi r^2 h\\)", "is_correct": False},
            {"text": "গ) \\(4\\pi r^2 h\\)", "is_correct": False},
            {"text": "ঘ) \\(\\pi r^2 h\\)", "is_correct": True}
        ]
    },
    {
        "serial": 50,
        "text": "পরিমাপের ক্ষেত্রে 'লঘিষ্ঠ ধ্রুবক' (Least count) যত কম হয়, যন্ত্রটি দিয়ে পরিমাপ তত কী হয়?",
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>লঘিষ্ঠ ধ্রুবক যত কম হয়, যন্ত্রের সাহায্যে তত সূক্ষ্ম বা নিখুঁত পরিমাপ পাওয়া যায়।",
        "options": [
            {"text": "ক) বেশি সূক্ষ্ম ও নিখুঁত হয়", "is_correct": True},
            {"text": "খ) বেশি ত্রুটিপূর্ণ হয়", "is_correct": False},
            {"text": "গ) কম নিখুঁت হয়", "is_correct": False},
            {"text": "ঘ) কোনো প্রভাব ফেলে না", "is_correct": False}
        ]
    },
    {
        "serial": 51,
        "text": "কোনো বস্তুর ভর m এবং এর উপাদানের ঘনত্ব \\(\\rho\\) হলে, বস্তুটির আয়তন V নির্ণয়ের সূত্র কোনটি?",
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>আমরা জানি, \\(\\rho = \\frac{m}{V}\\), সুতরাং আয়তন \\(V = \\frac{m}{\\rho}\\)।",
        "options": [
            {"text": "ক) \\(V = m \\times \\rho\\)", "is_correct": False},
            {"text": "খ) \\(V = \\frac{m}{\\rho}\\)", "is_correct": True},
            {"text": "গ) \\(V = \\frac{\\rho}{m}\\)", "is_correct": False},
            {"text": "ঘ) \\(V = m - \\rho\\)", "is_correct": False}
        ]
    },
    {
        "serial": 52,
        "text": "আন্তর্জাতিক একক পদ্ধতি (SI)-তে সময়ের একক কী?",
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>সময়ের এসআই একক হলো সেকেন্ড (s)।",
        "options": [
            {"text": "ক) মিনিট", "is_correct": False},
            {"text": "খ) ঘণ্টা", "is_correct": False},
            {"text": "গ) সেকেন্ড", "is_correct": True},
            {"text": "ঘ) দিন", "is_correct": False}
        ]
    },
    {
        "serial": 53,
        "text": "নিচের কোনটি লব্ধ রাশির উদাহরণ?",
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ত্বরণ হলো একটি লব্ধ রাশি, কারণ এটি বেগ ও সময়ের ওপর নির্ভরশীল। অন্যদিকে দৈর্ঘ্য, ভর ও সময় হলো মৌলিক রাশি।",
        "options": [
            {"text": "ক) দৈর্ঘ্য", "is_correct": False},
            {"text": "খ) ভর", "is_correct": False},
            {"text": "গ) তাপমাত্রা", "is_correct": False},
            {"text": "ঘ) ত্বরণ", "is_correct": True}
        ]
    },
    {
        "serial": 54,
        "text": "একটি আদর্শ পরিমাপের ক্ষেত্রে নিচের কোন শর্তটি অপরিহার্য?<br>i. পরিমাপের একটি সুবিধাজনক একক থাকতে হবে<br>ii. এককের মান সকলের কাছে স্পষ্ট ও নির্দিষ্ট হতে হবে<br>iii. পরিমাপটি সবসময় নিখুঁত ও ত্রুটিমুক্ত হতে হবে<br>নিচের কোনটি সঠিক?",
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>একটি গ্রহণযোগ্য পরিমাপের জন্য সুবিধাজনক একক থাকা এবং তার মান সর্বজনস্বীকৃত ও নির্দিষ্ট হওয়া আবশ্যক। তবে শতভাগ ত্রুটিমুক্ত পরিমাপ প্রায় অসম্ভব, তাই সাধারণ কাঠামোর বিচারে i ও ii সঠিক।",
        "options": [
            {"text": "ক) i ও ii", "is_correct": True},
            {"text": "খ) i ও iii", "is_correct": False},
            {"text": "গ) ii ও iii", "is_correct": False},
            {"text": "ঘ) i, ii ও iii", "is_correct": False}
        ]
    },
    {
        "serial": 55,
        "text": "\\(5.67 \\times 10^{-4}\\)-এ সার্থক অঙ্কের সংখ্যা কয়টি?",
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>এখানে 5, 6 এবং 7—এই তিনটি অঙ্কই সার্থক অঙ্ক। বৈজ্ঞানিক রূপের ঘাত অংশটি সার্থক অঙ্ক নির্ধারণে ভূমিকা রাখে না।",
        "options": [
            {"text": "ক) ৪টি", "is_correct": False},
            {"text": "খ) ৩টি", "is_correct": True},
            {"text": "গ) ২টি", "is_correct": False},
            {"text": "ঘ) ৫টি", "is_correct": False}
        ]
    },
    {
        "serial": 56,
        "text": "ত্বরণের মাত্রা সমীকরণ নিচের কোনটি?",
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ত্বরণ = বেগ / সময় = \\(\\frac{\\text{সরণ/সময়}}{\\text{সময়}} = \\frac{[LT^{-1}]}{[T]} = [LT^{-2}]\\)।",
        "options": [
            {"text": "ক) \\([LT^{-1}]\\)", "is_correct": False},
            {"text": "খ) \\([MLT^{-2}]\\)", "is_correct": False},
            {"text": "গ) \\([LT^{-2}]\\)", "is_correct": True},
            {"text": "ঘ) \\([ML^2T^{-2}]\\)", "is_correct": False}
        ]
    },
    {
        "serial": 57,
        "text": "মেট্রিক পদ্ধতিতে ভরের মূল একক কোনটি?",
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>এসআই বা মেট্রিক পদ্ধতিতে ভরের মূল বা প্রমিত একক হলো কিলোগ্রাম (kg)।",
        "options": [
            {"text": "ক) গ্রাম", "is_correct": False},
            {"text": "খ) মিলিগ্রাম", "is_correct": False},
            {"text": "গ) টন", "is_correct": False},
            {"text": "ঘ) কিলোগ্রাম", "is_correct": True}
        ]
    },
    {
        "serial": 58,
        "text": "একটি নিরেট লোহার গোলকের ব্যাসার্ধ \\(r = 2 \\text{ cm}\\) হলে এর আয়তন কত হবে? (\\(\\pi \\approx 3.1416\\))",
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>\\(V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3} \\times 3.1416 \\times (2)^3 = \\frac{4 \\times 3.1416 \\times 8}{3} \\approx 33.51 \\text{ cm}^3\\)।",
        "options": [
            {"text": "ক) 33.51 cm³", "is_correct": True},
            {"text": "খ) 12.56 cm³", "is_correct": False},
            {"text": "গ) 25.13 cm³", "is_correct": False},
            {"text": "ঘ) 50.26 cm³", "is_correct": False}
        ]
    },
    {
        "serial": 59,
        "text": "কোনো রাশি পরিমাপের সময় পরীক্ষকের চোখের ভুল অবস্থানের কারণে যে ত্রুটির সৃষ্টি হয়, তাকে কী বলে?",
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>স্কেলের পাঠ নেওয়ার সময় চোখের দৃষ্টি সঠিকভাবে লম্বভাবে না রেখে বাঁকাভাবে রাখলে যে ত্রুটি হয়, তাকে **লম্বন ত্রুটি (Parallax error)** বলে।",
        "options": [
            {"text": "ক) যান্ত্রিক ত্রুটি", "is_correct": False},
            {"text": "খ) লম্বন ত্রুটি", "is_correct": True},
            {"text": "গ) শূন্য ত্রুটি", "is_correct": False},
            {"text": "ঘ) যাদৃচ্ছিক ত্রুটি", "is_correct": False}
        ]
    },
    {
        "serial": 60,
        "text": "পদার্থবিজ্ঞানে পরিমাপের গুরুত্ব অপরিসীম। নিচে কোন ক্ষেত্রগুলোতে পরিমাপ সরাসরি জড়িত?<br>i. বৈজ্ঞানিক তত্ত্ব বা সূত্র পরীক্ষা ও যাচাইকরণে<br>ii. দৈনন্দিন কেনাকাটা ও বাণিজ্যিকভাবে পণ্য আদান-প্রদানে<br>iii. নিখুঁত প্রকৌশল ও চিকিৎসাবিজ্ঞানের নানাবিধ যন্ত্র ব্যবহারে<br>নিচের কোনটি সঠিক?",
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>বিজ্ঞান, বাণিজ্য, প্রকৌশল এবং চিকিৎসাবিজ্ঞান—প্রতিটি ক্ষেত্রেই সঠিক পরিমাপ অপরিহার্য। প্রদত্ত তিনটি বিবৃতিই সঠিক।",
        "options": [
            {"text": "ক) i ও ii", "is_correct": False},
            {"text": "খ) i ও iii", "is_correct": False},
            {"text": "গ) ii ও iii", "is_correct": False},
            {"text": "ঘ) i, ii ও iii", "is_correct": True}
        ]
    }
]

for data in mcq_data_part4_physics_ch1:
    q, created = Question.objects.update_or_create(
        quiz=quiz_instance,
        serial_number=data["serial"],
        defaults={
            'text': data["text"],
            'question_type': 'mcq',
            'explanation': data["explanation"],
            'order_number': data["serial"],
            'loop_serial': data["serial"]
        }
    )
    
    q.options.all().delete()
    
    for opt in data["options"]:
        Option.objects.create(
            question=q,
            text=opt["text"],
            is_correct=opt["is_correct"]
        )

total_q = Question.objects.filter(quiz=quiz_instance).count()
print(f"🎉 পদার্থবিজ্ঞান প্রথম অধ্যায়ের পার্ট-৪ সফলভাবে সংশোধন ও আপডেট হয়েছে! Chapter ID (2) এ বর্তমানে মোট {total_q}টি MCQ সংরক্ষিত আছে।")