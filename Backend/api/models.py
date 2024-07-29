from django.db import models
import random

# Create your models here.
class Addemployee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    
    department = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    join_date = models.DateField()
    position = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=6, unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_unique_employee_id()
        super(Addemployee, self).save(*args, **kwargs)

    def generate_unique_employee_id(self):
        while True:
            employee_id = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            if not Addemployee.objects.filter(employee_id=employee_id).exists():
                return employee_id

    def _str_(self):
        return self.name


class Users(models.Model):
    user_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)
    
    def __str__(self):
        return f'User: {self.user_id}'
    
    
    