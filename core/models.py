# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

# نموذج المستخدم المخصص (Custom User Model)
# يرث من AbstractUser لإضافة حقول مخصصة مع الحفاظ على نظام المصادقة الأساسي لـ Django
class User(AbstractUser):
    # تعريف الخيارات لنوع الصلاحية
    PERMISSION_CHOICES = (
        ('admin', 'Admin'), # مسؤول
        ('user', 'User'),   # مستخدم عادي
    )

    # الحقول الإضافية لنموذج المستخدم
    full_name = models.CharField(max_length=255, verbose_name="الاسم الكامل")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="البلد")
    governorate = models.CharField(max_length=100, blank=True, null=True, verbose_name="المحافظة")
    permission_type = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default='user', verbose_name="نوع الصلاحية")
    flash_drive_key = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name="مفتاح الفلاش")
    account_expiry_date = models.DateField(blank=True, null=True, verbose_name="تاريخ انتهاء الحساب")

    # دالة لإنشاء أو إعادة إنشاء مفتاح فلاش فريد للمستخدم
    def generate_flash_key(self):
        # يتم استخدام uuid4 لضمان أن المفتاح فريد وعشوائي
        self.flash_drive_key = uuid.uuid4().hex
        self.save()

    def __str__(self):
        return self.username

# نموذج صور السلايدر في الصفحة الرئيسية
class SliderImage(models.Model):
    image = models.ImageField(upload_to='sliders/', verbose_name="الصورة")
    caption = models.TextField(blank=True, verbose_name="النص المصاحب")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")

    def __str__(self):
        return f"Slider Image {self.id}"

# نموذج روابط التواصل الاجتماعي
class SocialLink(models.Model):
    name = models.CharField(max_length=50, verbose_name="الاسم (مثال: Facebook)")
    url = models.URLField(verbose_name="الرابط")
    icon_class = models.CharField(max_length=50, verbose_name="فئة الأيقونة (مثال: fab fa-facebook)")
    is_visible = models.BooleanField(default=True, verbose_name="مرئي؟")

    def __str__(self):
        return self.name

# نموذج الخدمات التي تقدمها الشركة
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    image = models.ImageField(upload_to='services/', verbose_name="صورة الخدمة")

    def __str__(self):
        return self.title

# نموذج شركة تصنيع السيارات
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم الشركة")

    def __str__(self):
        return self.name

# نموذج موديل السيارة (مرتبط بشركة)
class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الموديل")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='models', verbose_name="الشركة")

    def __str__(self):
        return f"{self.company.name} - {self.name}"

# نموذج السيارة (يحتوي على تفاصيل قطعة الغيار)
# class Car(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="الشركة")
#     model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="الموديل")
#     manufacturer = models.CharField(max_length=100, verbose_name="الصانع")
#     year = models.IntegerField(verbose_name="السنة")
#     part_number = models.CharField(max_length=100, verbose_name="رقم القطعة")
#     crash_in = models.CharField(max_length=100, verbose_name="Crash In")


#     def __str__(self):
#         return f"{self.company.name} {self.model.name} ({self.year}) - {self.part_number}"

class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="الشركة")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="الموديل")
    manufacturer = models.CharField(max_length=100, verbose_name="الصانع")
    year = models.IntegerField(verbose_name="السنة")
    part_number = models.CharField(max_length=100, verbose_name="رقم القطعة")
    crash_in = models.CharField(max_length=100, verbose_name="Crash In")

    id_chep = models.CharField(max_length=100, verbose_name="ID Chep", null=True, blank=True)
    read = models.CharField(max_length=255, verbose_name="Read", null=True, blank=True)
    write = models.CharField(max_length=255, verbose_name="Write", null=True, blank=True)

    def __str__(self):
        return f"{self.company.name} {self.model.name} ({self.year})"


# نموذج لإعدادات مظهر الموقع
class SiteAppearance(models.Model):
    # حقل لتخزين صورة خلفية صفحة تسجيل الدخول
    login_background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True, verbose_name="صورة خلفية تسجيل الدخول")

    def __str__(self):
        return "Site Appearance Settings"
