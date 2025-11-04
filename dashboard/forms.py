# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import User, Service, SliderImage, SocialLink, Company, CarModel, SiteAppearance
from core.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'company', 'model', 'manufacturer', 'year', 
            'part_number', 'crash_in', 
            'id_chep', 'read', 'write'
        ]
        widgets = {
            'company': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.Select(attrs={'class': 'form-select'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الصانع'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سنة الصنع'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم القطعة'}),
            'crash_in': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مكان التصادم'}),
            'id_chep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل ID Chep إن وُجد'}),
            'read': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Read data'}),
            'write': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write data'}),
        }
# نموذج مخصص لإنشاء مستخدم جديد، يرث من UserCreationForm المدمج
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User # تحديد النموذج
        # تحديد الحقول التي ستظهر في النموذج
        fields = ('username', 'email', 'full_name', 'phone_number', 'country', 'governorate', 'permission_type', 'account_expiry_date')

# نموذج مخصص لتعديل مستخدم حالي، يرث من UserChangeForm المدمج
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        # استبعاد حقل كلمة المرور من نموذج التعديل لتبسيطه
        fields = ('username', 'email', 'full_name', 'phone_number', 'country', 'governorate', 'permission_type', 'account_expiry_date', 'is_active')

# نموذج لإدارة الخدمات (Service)
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__' # تضمين جميع حقول النموذج

# نموذج لإدارة صور السلايدر (SliderImage)
class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = '__all__'

# نموذج لإدارة روابط التواصل الاجتماعي (SocialLink)
class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'

# نموذج لإدارة الشركات (Company)
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

# نموذج لإدارة موديلات السيارات (CarModel)
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

# نموذج لإدارة مظهر الموقع (SiteAppearance)
class SiteAppearanceForm(forms.ModelForm):
    class Meta:
        model = SiteAppearance
        fields = ['login_background_image'] # تضمين حقل صورة الخلفية فقط
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
