#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# -*- coding: utf-8 -*-
# السطر أعلاه يضمن أن الملف يُعامل بترميز UTF-8، وهو أمر مهم لدعم اللغة العربية في التعليقات.

# استيراد الوحدات اللازمة من المكتبات القياسية
import os
import sys

def main():
    """Run administrative tasks."""
    # تعيين متغير البيئة DJANGO_SETTINGS_MODULE ليشير إلى ملف إعدادات المشروع.
    # هذا يخبر Django أين يجد الإعدادات الخاصة بمشروعك.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_parts_management.settings')
    try:
        # محاولة استيراد دالة execute_from_command_line من Django.
        # هذه الدالة هي المسؤولة عن تنفيذ الأوامر الإدارية (مثل runserver, migrate, etc.).
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # إذا فشل استيراد Django، يتم رفع خطأ يوضح أن Django قد لا يكون مثبتًا أو متاحًا.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # تنفيذ الأمر الذي تم تمريره عبر سطر الأوامر.
    # sys.argv هي قائمة تحتوي على وسائط سطر الأوامر.
    execute_from_command_line(sys.argv)

# التحقق مما إذا كان الملف هو البرنامج الرئيسي الذي يتم تشغيله.
# هذا يضمن أن دالة main() لا تُستدعى إلا عند تشغيل الملف مباشرة.
if __name__ == '__main__':
    main()
