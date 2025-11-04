# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, FormView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from core.models import Car
from .forms import CarForm,CarSearchForm
# استيراد النماذج والنماذج (Forms) والمزخرفات (Decorators)
from core.models import User, Service, SliderImage, SocialLink, Company, CarModel, SiteAppearance
from .forms import (
    CustomUserCreationForm, CustomUserChangeForm, ServiceForm, SliderImageForm, 
    SocialLinkForm, CompanyForm, CarModelForm, SiteAppearanceForm
)
from .decorators import admin_required

# Mixin للتحقق من أن المستخدم هو مسؤول
# هذا يضمن أن جميع الواجهات التي ترث منه محمية
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.permission_type == 'admin'

# الصفحة الرئيسية للوحة التحكم
class DashboardHomeView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = User.objects.count()
        context['car_count'] = Car.objects.count()
        context['company_count'] = Company.objects.count()
        return context

# --- إدارة المستخدمين ---
class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/user_list.html'
    context_object_name = 'users'

class UserCreateView(AdminRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'dashboard/user_form.html'
    success_url = reverse_lazy('dashboard:user_list')

class UserUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'dashboard/user_form.html'
    success_url = reverse_lazy('dashboard:user_list')

class UserDeleteView(AdminRequiredMixin, DeleteView):
    model = User
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:user_list')

# واجهة وظيفية لإنشاء مفتاح فلاش
@admin_required
def generate_user_flash_key(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.permission_type == 'user':
        user.generate_flash_key()
        messages.success(request, f"تم إنشاء مفتاح فلاش جديد للمستخدم {user.username}")
    else:
        messages.error(request, "لا يمكن إنشاء مفتاح فلاش للمسؤولين.")
    return redirect('dashboard:user_list')

# --- CRUD لـ Service ---
class ServiceListView(AdminRequiredMixin, ListView):
    model = Service
    template_name = 'dashboard/service_list.html'
    context_object_name = 'services'

class ServiceCreateView(AdminRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard:service_list')

class ServiceUpdateView(AdminRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard:service_list')

class ServiceDeleteView(AdminRequiredMixin, DeleteView):
    model = Service
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:service_list')

# --- CRUD لـ SliderImage ---
class SliderImageListView(AdminRequiredMixin, ListView):
    model = SliderImage
    template_name = 'dashboard/slider_list.html'
    context_object_name = 'sliders'

class SliderImageCreateView(AdminRequiredMixin, CreateView):
    model = SliderImage
    form_class = SliderImageForm
    template_name = 'dashboard/slider_form.html'
    success_url = reverse_lazy('dashboard:slider_list')

class SliderImageUpdateView(AdminRequiredMixin, UpdateView):
    model = SliderImage
    form_class = SliderImageForm
    template_name = 'dashboard/slider_form.html'
    success_url = reverse_lazy('dashboard:slider_list')

class SliderImageDeleteView(AdminRequiredMixin, DeleteView):
    model = SliderImage
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:slider_list')

# --- CRUD لـ SocialLink ---
class SocialLinkListView(AdminRequiredMixin, ListView):
    model = SocialLink
    template_name = 'dashboard/social_link_list.html'
    context_object_name = 'social_links'

class SocialLinkCreateView(AdminRequiredMixin, CreateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = 'dashboard/social_link_form.html'
    success_url = reverse_lazy('dashboard:social_link_list')

class SocialLinkUpdateView(AdminRequiredMixin, UpdateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = 'dashboard/social_link_form.html'
    success_url = reverse_lazy('dashboard:social_link_list')

class SocialLinkDeleteView(AdminRequiredMixin, DeleteView):
    model = SocialLink
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:social_link_list')

# --- CRUD لـ Company ---
class CompanyListView(AdminRequiredMixin, ListView):
    model = Company
    template_name = 'dashboard/company_list.html'
    context_object_name = 'companies'

class CompanyCreateView(AdminRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'dashboard/company_form.html'
    success_url = reverse_lazy('dashboard:company_list')

class CompanyUpdateView(AdminRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'dashboard/company_form.html'
    success_url = reverse_lazy('dashboard:company_list')

class CompanyDeleteView(AdminRequiredMixin, DeleteView):
    model = Company
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:company_list')

# --- CRUD لـ CarModel ---
class CarModelListView(AdminRequiredMixin, ListView):
    model = CarModel
    template_name = 'dashboard/carmodel_list.html'
    context_object_name = 'carmodels'

class CarModelCreateView(AdminRequiredMixin, CreateView):
    model = CarModel
    form_class = CarModelForm
    template_name = 'dashboard/carmodel_form.html'
    success_url = reverse_lazy('dashboard:carmodel_list')

class CarModelUpdateView(AdminRequiredMixin, UpdateView):
    model = CarModel
    form_class = CarModelForm
    template_name = 'dashboard/carmodel_form.html'
    success_url = reverse_lazy('dashboard:carmodel_list')

class CarModelDeleteView(AdminRequiredMixin, DeleteView):
    model = CarModel
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:carmodel_list')

# 🔹 عرض قائمة السيارات
# 🔹 عرض قائمة السيارات
class CarListView(AdminRequiredMixin, ListView):
    model = Car
    template_name = 'dashboard/car_list.html'
    context_object_name = 'cars'
    paginate_by = 10
    def get_queryset(self):
        # الحصول على مجموعة البيانات الأساسية (كل السيارات)
        queryset = super().get_queryset()
        # الحصول على بيانات البحث والفلترة من طلب GET
        query = self.request.GET.get('query')
        company_id = self.request.GET.get('company')
        model_id = self.request.GET.get('model')

        # تطبيق فلتر البحث العام إذا كان موجودًا
        if query:
            # البحث في عدة حقول باستخدام Q objects
            queryset = queryset.filter(
                Q(manufacturer__icontains=query) |
                Q(year__icontains=query) |
                Q(part_number__icontains=query) |
                Q(crash_in__icontains=query)
            )
        
        # تطبيق فلتر الشركة إذا كان موجودًا
        if company_id:
            queryset = queryset.filter(company_id=company_id)

        # تطبيق فلتر الموديل إذا كان موجودًا
        if model_id:
            queryset = queryset.filter(model_id=model_id)

        return queryset.order_by('company__name', 'model__name') # ترتيب النتائج

    # دالة لإضافة بيانات إضافية إلى السياق
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # إضافة نموذج البحث إلى السياق لعرضه في القالب
        context['search_form'] = CarSearchForm(self.request.GET)
        return context
# واجهة عرض تفاصيل سيارة واحدة
class CarDetailView(AdminRequiredMixin, DetailView):
    model = Car # النموذج الذي سيتم عرض تفاصيله
    template_name = 'main/car_detail.html' # القالب المستخدم
    context_object_name = 'car' # اسم المتغير في القالب


# 🔹 إنشاء سيارة جديدة
class CarCreateView(AdminRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'dashboard/car_form.html'
    success_url = reverse_lazy('dashboard:car_list')


# 🔹 تعديل سيارة
class CarUpdateView(AdminRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'dashboard/car_form.html'
    success_url = reverse_lazy('dashboard:car_list')


# 🔹 حذف سيارة
class CarDeleteView(AdminRequiredMixin, DeleteView):
    model = Car
    template_name = 'dashboard/car_confirm_delete.html'
    success_url = reverse_lazy('dashboard:car_list')


# 🔹 عرض تفاصيل سيارة
class CarDetailView(AdminRequiredMixin, DetailView):
    model = Car
    template_name = 'dashboard/car_detail.html'
    context_object_name = 'car'


class CarDoItView(AdminRequiredMixin, DetailView):
    model = Car
    template_name = 'dashboard/car_do_it.html'
    context_object_name = 'car'

# --- إدارة المظهر ---
class SiteAppearanceUpdateView(AdminRequiredMixin, FormView):
    form_class = SiteAppearanceForm
    template_name = 'dashboard/appearance_form.html'
    success_url = reverse_lazy('dashboard:appearance_update')

    def get_object(self):
        # الحصول على كائن الإعدادات أو إنشائه إذا لم يكن موجودًا
        obj, created = SiteAppearance.objects.get_or_create(pk=1)
        return obj

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "تم تحديث صورة الخلفية بنجاح.")
        return super().form_valid(form)
