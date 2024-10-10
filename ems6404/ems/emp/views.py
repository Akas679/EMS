from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Employee, LeaveRequest, Complaint, Attendance
from django.http import JsonResponse

# Login function
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if role == 'admin':
                return redirect('admin-site')  # Redirect to admin dashboard
            elif role == 'employee':
                return redirect('employee-dashboard')  # Redirect to employee dashboard
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'employee_information/login.html')

# Employee dashboard
@login_required
def employee_dashboard(request):
    return render(request, 'emp/employee_dashboard.html')


# View employee details
@login_required
def employee_details(request):
    # If you want to get the employee details of the logged-in user
    return render(request, 'emp/view_details.html') # Assuming there's a OneToOne relationship with User

   
# Update profile
@login_required
def update_profile(request, employee_id):
    # Fetch the employee object
   return render(request, 'emp/update.html')

    
@login_required
def view_attendance_report(request):
      return render(request, 'emp/viewAttendanceReport.html')


# View leave status
@login_required
def view_leave_status(request):
      return render(request, 'emp/view_leaves_status.html')
# Logout user
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


# Apply for leave
@login_required
def apply_for_leave(request):
      return render(request, 'emp/apply_for_leaves.html')

# Raised complaint
@login_required
def raised_complaint(request):
    return render(request, 'emp/emp_complaint.html')
