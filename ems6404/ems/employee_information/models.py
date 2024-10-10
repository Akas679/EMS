from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# No need to import Employees since it's already in this file
# from employee_information.models import Employees 
# employee_information/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

from django.db import models

class LeaveRequest(models.Model):
    # Define your leave types as choices
    LEAVE_TYPE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('annual', 'Annual Leave'),
        ('maternity', 'Maternity Leave'),
        ('paternity', 'Paternity Leave'),
        ('bereavement', 'Bereavement Leave'),
        ('unpaid', 'Unpaid Leave'),
    ]

    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPE_CHOICES,
        default='sick',  # Optional: set a default value
    )

    # Other fields
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"


class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Employees(models.Model):
    code = models.CharField(max_length=100, blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True, null=True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True, null=True) 
    dob = models.DateField(blank=True, null=True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname + ' '
    

