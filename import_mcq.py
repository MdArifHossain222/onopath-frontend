import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onopath_backend.settings')
django.setup()

from core.models import Quiz, Question, Option, Chapter

# Chapter 14
target_chapter = Chapter.objects.get(id=26)
quiz_instance = Quiz.objects.get(chapter=target_chapter)

questions_data = [

    {
        "serial": 141,
        "text": "জীববিজ্ঞান ও পদার্থবিজ্ঞানের সমন্বয়ে গড়ে ওঠা শাখাটিকে কী বলা হয়?",
        "options": [
            {"text": "ক) ভূ-পদার্থবিজ্ঞান", "is_correct": False},
            {"text": "খ) জ্যোতির্পদার্থবিজ্ঞান", "is_correct": False},
            {"text": "গ) জীবপদার্থবিজ্ঞান", "is_correct": True},
            {"text": "ঘ) তাপগতিবিজ্ঞান", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>জীববিজ্ঞানের বিভিন্ন ঘটনা ও প্রক্রিয়া বোঝার জন্য পদার্থবিজ্ঞানের নীতি ব্যবহার করা হলে তাকে জীবপদার্থবিজ্ঞান বা Biophysics বলা হয়।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) ভূ-পদার্থবিজ্ঞান পৃথিবীর ভৌত বৈশিষ্ট্য নিয়ে আলোচনা করে।<br>খ) জ্যোতির্পদার্থবিজ্ঞান মহাকাশীয় বস্তুর ভৌত বৈশিষ্ট্য নিয়ে আলোচনা করে।<br>গ) সঠিক—জীববিজ্ঞান ও পদার্থবিজ্ঞানের সমন্বয়ই জীবপদার্থবিজ্ঞান।<br>ঘ) তাপগতিবিজ্ঞান তাপ ও শক্তির রূপান্তর নিয়ে আলোচনা করে।<br><br><strong>মনে রাখবে:</strong> Biology + Physics = Biophysics।"
    },

    {
        "serial": 142,
        "text": "জগদীশচন্দ্র বসুর উদ্ভিদ নিয়ে গবেষণায় কোন যন্ত্রটি বিশেষভাবে গুরুত্বপূর্ণ ছিল?",
        "options": [
            {"text": "ক) ক্রেসকোগ্রাফ", "is_correct": True},
            {"text": "খ) স্টেথোস্কোপ", "is_correct": False},
            {"text": "গ) থার্মোমিটার", "is_correct": False},
            {"text": "ঘ) ব্যারোমিটার", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>জগদীশচন্দ্র বসু উদ্ভিদের বৃদ্ধি ও উদ্দীপনার প্রতি প্রতিক্রিয়া পর্যবেক্ষণ ও পরিমাপের জন্য ক্রেসকোগ্রাফ ব্যবহার করেছিলেন।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) সঠিক—ক্রেসকোগ্রাফ উদ্ভিদের অতি ক্ষুদ্র বৃদ্ধি পরিমাপ করতে ব্যবহৃত হয়।<br>খ) স্টেথোস্কোপ সাধারণত হৃদস্পন্দন ও শ্বাসপ্রশ্বাসের শব্দ শোনার জন্য ব্যবহৃত হয়।<br>গ) থার্মোমিটার তাপমাত্রা পরিমাপ করে।<br>ঘ) ব্যারোমিটার বায়ুচাপ পরিমাপ করে।<br><br><strong>মনে রাখবে:</strong> জগদীশচন্দ্র বসু → উদ্ভিদ → ক্রেসকোগ্রাফ।"
    },

    {
        "serial": 143,
        "text": "একজন চিকিৎসক যদি কোনো অঙ্গের বৈদ্যুতিক কার্যকলাপ সম্পর্কে জানতে চান, তাহলে কোন ধরনের পরীক্ষার ধারণাটি সবচেয়ে উপযুক্ত?",
        "options": [
            {"text": "ক) এন্ডোস্কপি", "is_correct": False},
            {"text": "খ) ECG বা EEG", "is_correct": True},
            {"text": "গ) আল্ট্রাসনোগ্রাফি", "is_correct": False},
            {"text": "ঘ) এক্স-রে", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>ECG হৃদপিণ্ডের বৈদ্যুতিক কার্যকলাপ এবং EEG মস্তিষ্কের বৈদ্যুতিক কার্যকলাপ রেকর্ড করে। তাই বৈদ্যুতিক কার্যকলাপ জানতে ECG বা EEG উপযুক্ত।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) এন্ডোস্কপি সরাসরি অভ্যন্তরীণ অঙ্গ পর্যবেক্ষণে ব্যবহৃত হয়।<br>খ) সঠিক—ECG ও EEG বৈদ্যুতিক কার্যকলাপ রেকর্ড করে।<br>গ) আল্ট্রাসনোগ্রাফি প্রতিফলিত শব্দতরঙ্গ ব্যবহার করে।<br>ঘ) এক্স-রে দেহের অভ্যন্তরীণ কাঠামোর ছবি তৈরিতে ব্যবহৃত হয়।<br><br><strong>মনে রাখবে:</strong> Electrical activity → ECG/EEG।"
    },

    {
        "serial": 144,
        "text": "কোনো রোগীর রক্তনালির কোথাও সংকোচন বা বাধা আছে কি না তা অনুসন্ধানে কোন প্রযুক্তিটি বেশি উপযোগী?",
        "options": [
            {"text": "ক) EEG", "is_correct": False},
            {"text": "খ) Crescograph", "is_correct": False},
            {"text": "গ) Angiography", "is_correct": True},
            {"text": "ঘ) ETT", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>Angiography রক্তনালির গঠন ও রক্তপ্রবাহ পর্যবেক্ষণে ব্যবহৃত হয়। তাই রক্তনালির সংকোচন বা বাধা শনাক্ত করতে এটি উপযোগী।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) EEG মস্তিষ্কের বৈদ্যুতিক কার্যকলাপ রেকর্ড করে।<br>খ) Crescograph উদ্ভিদের বৃদ্ধি পরিমাপে ব্যবহৃত হয়।<br>গ) সঠিক—Angiography রক্তনালির পরীক্ষা করে।<br>ঘ) ETT ব্যায়াম বা পরিশ্রমের সময় হৃদপিণ্ডের কর্মক্ষমতা পরীক্ষা করে।<br><br><strong>মনে রাখবে:</strong> Angiography → রক্তনালি।"
    },

    {
        "serial": 145,
        "text": "নিচের কোন পরীক্ষায় আয়নাইজিং বিকিরণ ব্যবহার না করেও দেহের অভ্যন্তরের ছবি পাওয়া যায়?",
        "options": [
            {"text": "ক) MRI", "is_correct": True},
            {"text": "খ) CT Scan", "is_correct": False},
            {"text": "গ) X-ray", "is_correct": False},
            {"text": "ঘ) Radiotherapy", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>MRI শক্তিশালী চৌম্বক ক্ষেত্র ও রেডিও তরঙ্গ ব্যবহার করে দেহের অভ্যন্তরের ছবি তৈরি করে। এতে X-ray ধরনের আয়নাইজিং বিকিরণ ব্যবহার করা হয় না।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) সঠিক—MRI-তে আয়নাইজিং বিকিরণ ব্যবহার করা হয় না।<br>খ) CT Scan X-ray ব্যবহার করে।<br>গ) X-ray নিজেই আয়নাইজিং বিকিরণ।<br>ঘ) Radiotherapy-তে চিকিৎসার উদ্দেশ্যে উচ্চশক্তির বিকিরণ ব্যবহার করা হয়।<br><br><strong>মনে রাখবে:</strong> MRI → Magnetic field + Radio wave → No ionizing radiation।"
    },

    {
        "serial": 146,
        "text": "আল্ট্রাসনোগ্রাফিতে কোনো অভ্যন্তরীণ কাঠামোর অবস্থান নির্ণয়ে কোন বিষয়টি বিশেষ গুরুত্বপূর্ণ?",
        "options": [
            {"text": "ক) প্রতিফলিত শব্দতরঙ্গ ফিরে আসতে যে সময় লাগে", "is_correct": True},
            {"text": "খ) X-ray-এর তীব্রতা", "is_correct": False},
            {"text": "গ) চৌম্বক ক্ষেত্রের দিক", "is_correct": False},
            {"text": "ঘ) রক্তে অক্সিজেনের পরিমাণ", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: ক</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>আল্ট্রাসনোগ্রাফিতে উচ্চ কম্পাঙ্কের শব্দতরঙ্গ দেহে পাঠানো হয়। বিভিন্ন টিস্যু থেকে প্রতিফলিত তরঙ্গ ফিরে আসে। এই প্রতিধ্বনি ফিরে আসতে কত সময় লাগে তা বিশ্লেষণ করে অভ্যন্তরীণ কাঠামোর অবস্থান বা গভীরতা সম্পর্কে ধারণা পাওয়া যায়।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) সঠিক—Echo-এর ফিরে আসার সময় থেকে অবস্থান নির্ণয় করা যায়।<br>খ) আল্ট্রাসনোগ্রাফিতে X-ray ব্যবহার করা হয় না।<br>গ) চৌম্বক ক্ষেত্র MRI-এর সঙ্গে সম্পর্কিত।<br>ঘ) রক্তে অক্সিজেনের পরিমাণ এই পদ্ধতির মূল নীতি নয়।<br><br><strong>মনে রাখবে:</strong> Ultrasound → Reflection/Echo → Time measurement।"
    },

    {
        "serial": 147,
        "text": "একজন রোগীর শরীরের কোনো অংশ সরাসরি ভেতর থেকে দেখে পরীক্ষা করতে হলে কোন পদ্ধতিটি সবচেয়ে উপযুক্ত?",
        "options": [
            {"text": "ক) CT Scan", "is_correct": False},
            {"text": "খ) Endoscopy", "is_correct": True},
            {"text": "গ) ECG", "is_correct": False},
            {"text": "ঘ) Radiotherapy", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>Endoscopy-তে endoscope নামের বিশেষ যন্ত্র ব্যবহার করে শরীরের নির্দিষ্ট অভ্যন্তরীণ অঙ্গ বা নালির ভেতরের অংশ সরাসরি পর্যবেক্ষণ করা যায়।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) CT Scan X-ray ও কম্পিউটার প্রক্রিয়াকরণের মাধ্যমে cross-sectional image তৈরি করে।<br>খ) সঠিক—Endoscopy সরাসরি অভ্যন্তরীণ অংশ পর্যবেক্ষণে ব্যবহৃত হয়।<br>গ) ECG হৃদপিণ্ডের বৈদ্যুতিক কার্যকলাপ রেকর্ড করে।<br>ঘ) Radiotherapy চিকিৎসার জন্য বিকিরণ ব্যবহার করে।<br><br><strong>মনে রাখবে:</strong> Direct internal observation → Endoscopy।"
    },

    {
        "serial": 148,
        "text": "নিচের কোন জোড়াটি রোগ নির্ণয় ও রোগের চিকিৎসার মধ্যে সঠিক পার্থক্য প্রকাশ করে?",
        "options": [
            {"text": "ক) Radiotherapy রোগ নির্ণয় করে এবং X-ray ক্যানসার চিকিৎসা করে", "is_correct": False},
            {"text": "খ) ECG ক্যানসার কোষ ধ্বংস করে এবং MRI হৃদপিণ্ডের চিকিৎসা করে", "is_correct": False},
            {"text": "গ) CT Scan রোগ নির্ণয়ে ব্যবহৃত হতে পারে এবং Radiotherapy চিকিৎসায় ব্যবহৃত হয়", "is_correct": True},
            {"text": "ঘ) Endoscopy সব ধরনের রোগের চিকিৎসা করে এবং EEG রোগ নির্ণয় করে না", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: গ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>CT Scan দেহের অভ্যন্তরের ছবি তৈরি করে রোগ নির্ণয়ে সহায়তা করে। অন্যদিকে Radiotherapy নির্দিষ্ট রোগ, বিশেষ করে ক্যানসারের চিকিৎসায় উচ্চশক্তির বিকিরণ ব্যবহার করে।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) Radiotherapy মূলত চিকিৎসার জন্য ব্যবহৃত হয়, আর X-ray রোগ নির্ণয়ে ব্যবহৃত হয়।<br>খ) ECG রোগ নির্ণয়ে হৃদপিণ্ডের বৈদ্যুতিক কার্যকলাপ রেকর্ড করে এবং MRI মূলত imaging-এর জন্য ব্যবহৃত হয়।<br>গ) সঠিক—CT diagnosis-এর জন্য এবং Radiotherapy treatment-এর জন্য ব্যবহৃত হয়।<br>ঘ) Endoscopy নির্দিষ্ট অভ্যন্তরীণ অংশ পর্যবেক্ষণে ব্যবহৃত হয় এবং EEG মস্তিষ্কের বৈদ্যুতিক কার্যকলাপ নির্ণয়ে গুরুত্বপূর্ণ।<br><br><strong>মনে রাখবে:</strong> Diagnosis এবং Treatment এক জিনিস নয়।"
    },

    {
        "serial": 149,
        "text": "নিচের কোন বক্তব্যটি চিকিৎসাক্ষেত্রে পদার্থবিজ্ঞানের ভূমিকা সবচেয়ে ভালোভাবে প্রকাশ করে?",
        "options": [
            {"text": "ক) পদার্থবিজ্ঞান শুধু রোগীর শরীরের তাপমাত্রা মাপতে ব্যবহৃত হয়", "is_correct": False},
            {"text": "খ) পদার্থবিজ্ঞানের নীতি ব্যবহার করে রোগ নির্ণয়, শরীরের কার্যকলাপ পর্যবেক্ষণ ও চিকিৎসা করা যায়", "is_correct": True},
            {"text": "গ) পদার্থবিজ্ঞান চিকিৎসাবিজ্ঞানের সঙ্গে সম্পর্কহীন", "is_correct": False},
            {"text": "ঘ) পদার্থবিজ্ঞান শুধু উদ্ভিদ গবেষণায় ব্যবহৃত হয়", "is_correct": False}
        ],
        "explanation": "<strong>সঠিক উত্তর: খ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>চিকিৎসাক্ষেত্রে পদার্থবিজ্ঞানের প্রয়োগ অত্যন্ত বিস্তৃত। X-ray, CT Scan, MRI, Ultrasonography, ECG, EEG, Angiography এবং Radiotherapy-এর মতো প্রযুক্তিতে পদার্থবিজ্ঞানের বিভিন্ন নীতি ব্যবহৃত হয়।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) পদার্থবিজ্ঞানের চিকিৎসাক্ষেত্রের প্রয়োগ শুধু তাপমাত্রা পরিমাপে সীমাবদ্ধ নয়।<br>খ) সঠিক—রোগ নির্ণয়, পর্যবেক্ষণ ও চিকিৎসা—সব ক্ষেত্রেই পদার্থবিজ্ঞানের প্রয়োগ রয়েছে।<br>গ) ভুল—চিকিৎসাবিজ্ঞানে পদার্থবিজ্ঞানের গুরুত্বপূর্ণ ভূমিকা রয়েছে।<br>ঘ) ভুল—উদ্ভিদ গবেষণার পাশাপাশি মানবদেহ ও চিকিৎসাতেও পদার্থবিজ্ঞান ব্যবহৃত হয়।<br><br><strong>মনে রাখবে:</strong> Physics → Diagnosis + Monitoring + Treatment।"
    },

    {
        "serial": 150,
        "text": "নিচের কোন সমন্বয়টি সঠিকভাবে প্রযুক্তি ও তার মূল কাজকে প্রকাশ করে?",
        "options": [
            {"text": "ক) EEG — রক্তনালির ছবি তৈরি", "is_correct": False},
            {"text": "খ) Endoscopy — মস্তিষ্কের বৈদ্যুতিক কার্যকলাপ রেকর্ড", "is_correct": False},
            {"text": "গ) Angiography — উদ্ভিদের বৃদ্ধি পরিমাপ", "is_correct": False},
            {"text": "ঘ) MRI — চৌম্বক ক্ষেত্র ও রেডিও তরঙ্গ ব্যবহার করে অভ্যন্তরীণ ছবি তৈরি", "is_correct": True}
        ],
        "explanation": "<strong>সঠিক উত্তর: ঘ</strong><br><strong>সহজ ব্যাখ্যা:</strong><br>MRI বা Magnetic Resonance Imaging শক্তিশালী চৌম্বক ক্ষেত্র ও রেডিও তরঙ্গ ব্যবহার করে দেহের অভ্যন্তরের বিস্তারিত ছবি তৈরি করে। তাই ঘ সঠিক।<br><br><strong>কেন অন্যগুলো ভুল:</strong><br>ক) EEG মস্তিষ্কের বৈদ্যুতিক কার্যকলাপ রেকর্ড করে; রক্তনালির পরীক্ষা Angiography-এর কাজ।<br>খ) Endoscopy অভ্যন্তরীণ অঙ্গ সরাসরি পর্যবেক্ষণে ব্যবহৃত হয়; মস্তিষ্কের বৈদ্যুতিক কার্যকলাপের জন্য EEG ব্যবহৃত হয়।<br>গ) Angiography রক্তনালির পরীক্ষা করে; উদ্ভিদের বৃদ্ধি পরিমাপের সঙ্গে এর সম্পর্ক নেই।<br>ঘ) সঠিক—MRI-এর মূল নীতি চৌম্বক ক্ষেত্র ও রেডিও তরঙ্গের সঙ্গে সম্পর্কিত।<br><br><strong>মনে রাখবে:</strong> MRI = Magnetic Resonance Imaging।"
    }
]

for data in questions_data:
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

print(f"Chapter 14 | Part-15 completed | Added/Updated: 10 MCQs | Total Questions: {total_q}")