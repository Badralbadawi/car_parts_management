# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة من Django
from django import forms

# استيراد النماذج من تطبيق core
from core.models import Company, CarModel
from core.models import User, Service, SliderImage, SocialLink, Company, CarModel, SiteAppearance
from core.models import Car

# نموذج تسجيل الدخول
class LoginForm(forms.Form):
    # حقل اسم المستخدم، من نوع CharField
    username = forms.CharField(
        label="اسم المستخدم", # النص الذي يظهر بجانب الحقل
        max_length=150, # أقصى عدد للحروف
        # تحديد السمات (attributes) لعنصر الإدخال في HTML
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل اسم المستخدم'})
    )
    # حقل كلمة المرور، من نوع CharField مع إخفاء النص
    password = forms.CharField(
        label="كلمة المرور",
        # استخدام PasswordInput لإخفاء الأحرف عند الكتابة
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'ادخل كلمة المرور'})
    )

# نموذج البحث عن السيارات
class CarSearchForm(forms.Form):
    # حقل البحث العام، ليس مطلوبًا (يمكن تركه فارغًا)
    query = forms.CharField(
        label="بحث عام",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ابحث عن صانع, سنة, رقم قطعة...'})
    )
    # حقل اختيار الشركة، ليس مطلوبًا
    # ModelChoiceField يعرض قائمة من كائنات نموذج معين
    company = forms.ModelChoiceField(
        label="الشركة",
        queryset=Company.objects.all(), # مصدر البيانات هو كل الشركات المسجلة
        required=False,
        empty_label="كل الشركات", # النص الذي يظهر للخيار الفارغ
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # حقل اختيار الموديل، ليس مطلوبًا
    model = forms.ModelChoiceField(
        label="الموديل",
        queryset=CarModel.objects.all(), # مصدر البيانات هو كل الموديلات المسجلة
        required=False,
        empty_label="كل الموديلات",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
