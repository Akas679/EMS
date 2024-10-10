from django.urls import path
from . import views
from .views import employee_dashboard

urlpatterns = [
     path('dashboard/', employee_dashboard, name='employee-dashboard'),  # This should match the name used in the button
    path('dashboard/', views.employee_dashboard, name='employee-dashboard'),
    path('view_details/', views.employee_details, name='employee-details'),
    path('apply_for_leaves/', views.apply_for_leave, name='apply-for-leaves'),
    path('update/', views.update_profile, name='update-profile'),
    path('view_attendance/', views.view_attendance_report, name='view-attendance'),
    path('view_leaves_status/', views.view_leave_status, name='view-leave-status'),
    path('apply_for_leaves/', views.apply_for_leave, name='apply-for-leaves'),
    path('emp_complaint/', views.raised_complaint, name='emp_complaint'),
    path('logout/', views.logout_user, name='logout'),
]
