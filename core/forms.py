from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'আপনার নাম'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ইমেইল'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['institution', 'phone_number', 'avatar']
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'শিক্ষাপ্রতিষ্ঠানের নাম'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ফোন নম্বর'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'profilePicInput', 'style': 'display: none;', 'accept': 'image/*'}),
        }