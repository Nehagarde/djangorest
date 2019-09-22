from django.shortcuts import render, get_object_or_404
from .serializers import EmployeeSerializer
from .models import Employees
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class EmployeesView(APIView):

    def get(self,request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self,request):
        employee = request.data.get('employees')
        serializer = EmployeeSerializer(data=employee)

        employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.username)})

    def patch(self,request,pk):
        saved_article = get_object_or_404(Employees.objects.all(), pk=pk)
        data = request.data.get('employees')
        serializer = Employees(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(employee_saved.username)})

