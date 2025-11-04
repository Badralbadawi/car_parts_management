from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # تسجيل الدخول
    path('login/', views.custom_login_view, name='login'),

    # تسجيل الخروج
    path('logout/', views.custom_logout_view, name='logout'),

    # قائمة السيارات
    path('cars/', views.CarListView.as_view(), name='car_list'),

    # تفاصيل السيارة
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]
