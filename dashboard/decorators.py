# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة من Django
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

# دالة للتحقق مما إذا كان المستخدم مسؤولاً (admin)
def is_admin(user):
    # يعود True إذا كان المستخدم مسجل دخوله ونوع صلاحيته 'admin'
    return user.is_authenticated and user.permission_type == 'admin'

# إنشاء مُزخرف (decorator) مخصص لحماية الواجهات التي تتطلب صلاحيات مسؤول
# user_passes_test هو مُزخرف مدمج في Django يأخذ دالة اختبار كوسيط
# login_url يحدد الصفحة التي سيتم توجيه المستخدم إليها إذا فشل الاختبار (لم يكن مسؤولاً)
admin_required = user_passes_test(is_admin, login_url='main:login')
