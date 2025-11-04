# -*- coding: utf-8 -*-
# استيراد الفئة AppConfig الأساسية من Django
from django.apps import AppConfig

# تعريف فئة التكوين لتطبيق 'core'
class CoreConfig(AppConfig):
    # نوع الحقل التلقائي للمفاتيح الأساسية في نماذج هذا التطبيق
    default_auto_field = 'django.db.models.BigAutoField'
    # اسم التطبيق
    name = 'core'
