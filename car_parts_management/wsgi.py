# -*- coding: utf-8 -*-
"""
WSGI config for car_parts_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# استيراد الوحدات اللازمة
import os

from django.core.wsgi import get_wsgi_application

# تعيين متغير البيئة ليشير إلى ملف إعدادات المشروع
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_parts_management.settings')

# الحصول على تطبيق WSGI الخاص بالمشروع
# WSGI (Web Server Gateway Interface) هو معيار لواجهات تطبيقات الويب المتزامنة في بايثون.
application = get_wsgi_application()
