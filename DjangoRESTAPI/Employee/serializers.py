from rest_framework import serializers
from Employee.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')


class EmployeeSerializer(serializers.ModelSerializers):
    class Meta:
        model = Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')