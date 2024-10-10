from django.contrib import admin
from django.urls import path, include
from employee_information import views as emp_views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin-site"),  # Admin panel URL
    path('emp/', include('emp.urls')),  # Employee app URLs
    path('admin_panel/', include('employee_information.urls')),  # Admin panel URLs
    path('login/', emp_views.login_user, name='login'),  # Custom login URL
    path('', emp_views.home, name='home-page'),  # Home page
]
