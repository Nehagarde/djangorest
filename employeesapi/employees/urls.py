from django.conf.urls import url
from django.urls import path

from .views import EmployeesView
app_name = 'employees'


urlpatterns = [
    url('employees/',EmployeesView.as_view()),
    path('employees/<int:pk>', EmployeesView.as_view()),
]