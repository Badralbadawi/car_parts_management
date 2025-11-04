# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة من Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# استيراد النماذج من ملف models.py في نفس التطبيق
from .models import (
    User, SliderImage, SocialLink, Service, 
    Company, CarModel, Car, SiteAppearance
)

# تخصيص عرض نموذج المستخدم في لوحة التحكم
class CustomUserAdmin(UserAdmin):
    # تحديد الحقول التي ستظهر في قائمة المستخدمين
    list_display = ('username', 'email', 'full_name', 'permission_type', 'is_staff')
    # إضافة الحقول المخصصة إلى مجموعات الحقول في صفحة تعديل المستخدم
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Info', {'fields': ('full_name', 'phone_number', 'country', 'governorate', 'permission_type', 'flash_drive_key', 'account_expiry_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Info', {'fields': ('full_name', 'phone_number', 'country', 'governorate', 'permission_type', 'flash_drive_key', 'account_expiry_date')}),
    )

# تسجيل النماذج في لوحة تحكم Django الافتراضية
# هذا يسمح بإدارة هذه النماذج من خلال واجهة /admin/
admin.site.register(User, CustomUserAdmin)
admin.site.register(SliderImage)
admin.site.register(SocialLink)
admin.site.register(Service)
admin.site.register(Company)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(SiteAppearance)
