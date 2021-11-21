from django.contrib import admin

from Employee.models import Departments, Employees

# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
