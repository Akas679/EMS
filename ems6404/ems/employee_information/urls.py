from . import views
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login/', views.login_user, name='login'),  # Ensure this has a trailing slash
    path('logout/', views.logoutuser, name="logout"),  # Ensure this has a trailing slash
    path('about/', views.about, name="about-page"),
    path('departments/', views.departments, name="department-page"),
    path('manage_departments/', views.manage_departments, name="manage_departments-page"),
    path('save_department/', views.save_department, name="save-department-page"),
    path('delete_department/', views.delete_department, name="delete-department"),
    path('positions/', views.positions, name="position-page"),
    path('manage_positions/', views.manage_positions, name="manage_positions-page"),
    path('save_position/', views.save_position, name="save-position-page"),
    path('delete_position/', views.delete_position, name="delete-position"),
    path('employees/', views.employees, name="employee-page"),
    path('manage_employees/', views.manage_employees, name="manage_employees-page"),
    path('save_employee/', views.save_employee, name="save-employee-page"),
    path('delete_employee/', views.delete_employee, name="delete-employee"),
    path('view_employee/', views.view_employee, name="view-employee-page"),
    path('leave_management/', views.leave_management, name='leave_management'),
]
