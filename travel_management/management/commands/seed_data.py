"""
Management command: seed_data
Seeds initial departments, sample employees, and an admin user.
Run: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from travel_management.models import Department, Employee


class Command(BaseCommand):
    help = 'Seed initial data: admin user, departments, sample employees'

    def handle(self, *args, **kwargs):
        self.stdout.write('\n🌱 Seeding initial data for NTC Travel Management System...\n')

        # ── 1. Create Admin User ──────────────────────────────────
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='admin123',
                email='admin@ntc.net.np',
                first_name='System',
                last_name='Administrator'
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin user created: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('⚠️  Admin user already exists.'))

        # ── 2. Create Departments ─────────────────────────────────
        departments_data = [
            'Technical Division',
            'Commercial Division',
            'Finance & Administration',
            'Customer Service',
            'Network Operations',
            'Information Technology',
            'Human Resources',
            'Internal Audit',
        ]

        created_depts = {}
        for dept_name in departments_data:
            dept, created = Department.objects.get_or_create(name=dept_name)
            created_depts[dept_name] = dept
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Department created: {dept_name}'))

        # ── 3. Create Sample Employees ────────────────────────────
        sample_employees = [
            {
                'employee_id': 'NTC-001',
                'name': 'Ram Bahadur Thapa',
                'name_nepali': 'राम बहादुर थापा',
                'position': 'Branch Manager',
                'department': 'Finance & Administration',
                'phone': '9858012345',
                'email': 'ram.thapa@ntc.net.np',
            },
            {
                'employee_id': 'NTC-002',
                'name': 'Sita Kumari Sharma',
                'name_nepali': 'सिता कुमारी शर्मा',
                'position': 'Senior Engineer',
                'department': 'Technical Division',
                'phone': '9858023456',
                'email': 'sita.sharma@ntc.net.np',
            },
            {
                'employee_id': 'NTC-003',
                'name': 'Hari Prasad Adhikari',
                'name_nepali': 'हरि प्रसाद अधिकारी',
                'position': 'Junior Engineer',
                'department': 'Network Operations',
                'phone': '9858034567',
                'email': 'hari.adhikari@ntc.net.np',
            },
            {
                'employee_id': 'NTC-004',
                'name': 'Gita Devi Panta',
                'name_nepali': 'गीता देवी पन्त',
                'position': 'Account Officer',
                'department': 'Finance & Administration',
                'phone': '9858045678',
                'email': 'gita.panta@ntc.net.np',
            },
            {
                'employee_id': 'NTC-005',
                'name': 'Krishna Bahadur Bista',
                'name_nepali': 'कृष्ण बहादुर बिष्ट',
                'position': 'Customer Service Officer',
                'department': 'Customer Service',
                'phone': '9858056789',
                'email': 'krishna.bista@ntc.net.np',
            },
            {
                'employee_id': 'NTC-006',
                'name': 'Laxmi Prasad Joshi',
                'name_nepali': 'लक्ष्मी प्रसाद जोशी',
                'position': 'Technical Officer',
                'department': 'Technical Division',
                'phone': '9858067890',
                'email': 'laxmi.joshi@ntc.net.np',
            },
        ]

        for emp_data in sample_employees:
            dept_name = emp_data.pop('department')
            dept = created_depts.get(dept_name)
            emp, created = Employee.objects.get_or_create(
                employee_id=emp_data['employee_id'],
                defaults={**emp_data, 'department': dept}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Employee created: {emp.name} ({emp.employee_id})'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  Employee already exists: {emp.name}'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Data seeding complete!\n'))
        self.stdout.write('─' * 50)
        self.stdout.write('  Login URL  : http://127.0.0.1:8000/login/')
        self.stdout.write('  Username   : admin')
        self.stdout.write('  Password   : admin123')
        self.stdout.write('─' * 50 + '\n')
