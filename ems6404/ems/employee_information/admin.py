from django.contrib import admin
from employee_information.models import Department, Position, Employees
from django.contrib.auth.models import Group

# Unregister the Group model if you want to customize or remove it
admin.site.unregister(Group)

# Register your models here
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'date_added')
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'date_added')
    search_fields = ('name',)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'department_id', 'position_id', 'date_hired', 'status')
    search_fields = ('firstname', 'lastname', 'department_id__name', 'position_id__name')



