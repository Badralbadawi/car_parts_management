# -*- coding: utf-8 -*-
# استيراد الوحدات اللازمة
from django.urls import path
from . import views

# تحديد اسم النطاق (namespace) لتجنب تضارب أسماء الـ URL
app_name = 'dashboard'

# قائمة بأنماط عناوين URL الخاصة بلوحة التحكم
urlpatterns = [
    # الصفحة الرئيسية للوحة التحكم
    path('', views.DashboardHomeView.as_view(), name='home'),

    # --- إدارة المستخدمين ---
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/generate-key/', views.generate_user_flash_key, name='user_generate_key'),

    # --- إدارة المحتوى ---
    # الخدمات
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # صور السلايدر
    path('sliders/', views.SliderImageListView.as_view(), name='slider_list'),
    path('sliders/create/', views.SliderImageCreateView.as_view(), name='slider_create'),
    path('sliders/<int:pk>/update/', views.SliderImageUpdateView.as_view(), name='slider_update'),
    path('sliders/<int:pk>/delete/', views.SliderImageDeleteView.as_view(), name='slider_delete'),

    # روابط التواصل الاجتماعي
    path('social-links/', views.SocialLinkListView.as_view(), name='social_link_list'),
    path('social-links/create/', views.SocialLinkCreateView.as_view(), name='social_link_create'),
    path('social-links/<int:pk>/update/', views.SocialLinkUpdateView.as_view(), name='social_link_update'),
    path('social-links/<int:pk>/delete/', views.SocialLinkDeleteView.as_view(), name='social_link_delete'),

    # --- إدارة البيانات ---
    # الشركات
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),

    # موديلات السيارات
    path('carmodels/', views.CarModelListView.as_view(), name='carmodel_list'),
    path('carmodels/create/', views.CarModelCreateView.as_view(), name='carmodel_create'),
    path('carmodels/<int:pk>/update/', views.CarModelUpdateView.as_view(), name='carmodel_update'),
    path('carmodels/<int:pk>/delete/', views.CarModelDeleteView.as_view(), name='carmodel_delete'),
    # --- إدارة السيارات ---
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
    # المسار الخاص بقائمة السيارات
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/do-it/', views.CarDoItView.as_view(), name='car_do_it'),

    # المسار الخاص بعرض تفاصيل سيارة معينة
    # <int:pk> يلتقط رقمًا صحيحًا من الـ URL ويمرره كـ 'pk' (Primary Key) إلى الواجهة
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),

    # --- إدارة المظهر ---
    path('appearance/', views.SiteAppearanceUpdateView.as_view(), name='appearance_update'),
]
