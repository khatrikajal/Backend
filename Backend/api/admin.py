from django.contrib import admin
from .models import Users,Addemployee

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'password','repassword')

admin.site.register(Users, UsersAdmin)

class AddemployeeAdmin(admin.ModelAdmin):
     list_display = (
        'name','department','salary','email','gender','phone_number','address','join_date','position','employee_id')
        
admin.site.register(Addemployee, AddemployeeAdmin)
