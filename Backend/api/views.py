from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, Addemployee
from .serializers import UserSerializer, UserloginSerializer, AddemployeeSerializer
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def userlogin(request):
    serializer = UserloginSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        password = serializer.validated_data['password']
        try:
            user = Users.objects.get(user_id=user_id)
            if user.password == password:
                return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def create_employee_list(request):
    if request.method == 'GET':
        employees = Addemployee.objects.all()
        serializer = AddemployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AddemployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            if employee:
                email_subject = 'Your Employee ID created successfully'
                email_body = f'Dear {employee.name},\n\nYour employee ID is {employee.employee_id}.'
                try:
                    send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [employee.email], fail_silently=False)
                except Exception as e:
                    logger.error(f"Error sending email: {e}")
                    return Response({"message": f"Employee created, but email failed: {str(e)}"}, status=status.HTTP_201_CREATED)
                return Response({"message": "Employee created successfully"}, status=status.HTTP_201_CREATED)
        logger.error(f"Error creating employee: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def update_employee_details(request, pk):
    try:
        employee = Addemployee.objects.get(pk=pk)
    except Addemployee.DoesNotExist:
        return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddemployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AddemployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(f"Error updating employee: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    try:
        employee = Addemployee.objects.get(pk=pk)
    except Addemployee.DoesNotExist:
        return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AddemployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AddemployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)