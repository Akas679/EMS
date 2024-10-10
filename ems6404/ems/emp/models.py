from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True)  # Add mobile number field
    dob = models.DateField(null=True, blank=True)  # Add date of birth field
    department = models.CharField(max_length=50, blank=True)  # Add department field\
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Complaint(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Complaint from {self.employee.username} on {self.submitted_at}'









class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)  # e.g., 'Present', 'Absent'

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"        
    


   
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    # Leave type choices defined within the model class with correct indentation
    LEAVE_TYPE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('annual', 'Annual Leave'),
        ('maternity', 'Maternity Leave'),
        ('paternity', 'Paternity Leave'),
        ('bereavement', 'Bereavement Leave'),
        ('unpaid', 'Unpaid Leave'),
    ]

    # Foreign key to User model (employee)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} ({self.status})"
