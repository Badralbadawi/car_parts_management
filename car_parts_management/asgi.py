# -*- coding: utf-8 -*-
"""
ASGI config for car_parts_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# استيراد الوحدات اللازمة
import os

from django.core.asgi import get_asgi_application

# تعيين متغير البيئة ليشير إلى ملف إعدادات المشروع
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_parts_management.settings')

# الحصول على تطبيق ASGI الخاص بالمشروع
# ASGI (Asynchronous Server Gateway Interface) هو معيار لواجهات تطبيقات الويب غير المتزامنة في بايثون.
application = get_asgi_application()
