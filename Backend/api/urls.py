from django.urls import path
from . import views

urlpatterns = [
    
    path("register/", views.register, name='register'),
    path("login/", views.userlogin, name='userlogin'),
    path("Employees/", views.create_employee_list, name='create_employee_list'),
    path("Employee/<int:pk>", views.update_employee_details, name='update_employee_details')
    
]
