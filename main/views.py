# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Q

# استيراد النماذج من تطبيق 'core'
from core.models import SliderImage, SocialLink, Service, Car, SiteAppearance, Company, CarModel

# استيراد النماذج من ملف forms.py
from .forms import LoginForm, CarSearchForm

# ------------------------------
# واجهة الصفحة الرئيسية (صفحة تسجيل الدخول)
# ------------------------------
class HomePageView(TemplateView):
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = SliderImage.objects.filter(is_active=True)
        context['social_links'] = SocialLink.objects.filter(is_visible=True)
        context['services'] = Service.objects.all()
        return context

# ------------------------------
# دالة تسجيل الدخول
# ------------------------------
def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('main:car_list')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.permission_type == 'user' and user.account_expiry_date and user.account_expiry_date < timezone.now().date():
                    form.add_error(None, "لقد انتهت صلاحية حسابك.")
                else:
                    login(request, user)
                    if user.permission_type == 'admin':
                        return redirect('dashboard:home')
                    return redirect('main:car_list')
            else:
                form.add_error(None, "اسم المستخدم أو كلمة المرور غير صحيحة.")

    appearance = SiteAppearance.objects.first()
    context = {'form': form, 'appearance': appearance}
    return render(request, 'main/login.html', context)

# ------------------------------
# دالة تسجيل الخروج
# ------------------------------
def custom_logout_view(request):
    logout(request)
    return redirect('main:login')

# ------------------------------
# قائمة السيارات
# ------------------------------
class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'main/car_list.html'
    context_object_name = 'cars'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        company_id = self.request.GET.get('company')
        model_id = self.request.GET.get('model')

        if query:
            queryset = queryset.filter(
                Q(manufacturer__icontains=query) |
                Q(year__icontains=query) |
                Q(part_number__icontains=query) |
                Q(crash_in__icontains=query)
            )
        if company_id:
            queryset = queryset.filter(company_id=company_id)
        if model_id:
            queryset = queryset.filter(model_id=model_id)

        return queryset.order_by('company__name', 'model__name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CarSearchForm(self.request.GET)
        return context

# ------------------------------
# تفاصيل سيارة
# ------------------------------
class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'main/car_detail.html'
    context_object_name = 'car'
