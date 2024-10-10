from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create default admin and employee users'

    def handle(self, *args, **kwargs):
        # Create Admin User
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'password': 'admin123'}
        )
        if created:
            admin_user.set_password('admin123')  # Set password
            admin_user.save()
            admin_group, _ = Group.objects.get_or_create(name='Admin')
            admin_user.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        # Create Employee User
        employee_user, created = User.objects.get_or_create(
            username='employee',
            defaults={'password': 'employeepass123'}
        )
        if created:
            employee_user.set_password('employeepass123')  # Set password
            employee_user.save()
            employee_group, _ = Group.objects.get_or_create(name='Employee')
            employee_user.groups.add(employee_group)
            self.stdout.write(self.style.SUCCESS('Employee user created'))
        else:
            self.stdout.write(self.style.WARNING('Employee user already exists'))
