from rest_framework import serializers
from .models import Users,Addemployee

class UserSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['user_id', 'password', 'repassword']

    def validate(self, data):
        password = data.get('password')
        repassword = data.get('repassword')
        
        if password != repassword:
            raise serializers.ValidationError("Passwords do not match")
        
        return data

    def create(self, validated_data):
        validated_data.pop('repassword')  
        user = Users.objects.create(**validated_data)
        return user
        
    
        
class UserloginSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=20)
    
class AddemployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addemployee
        fields = '__all__'
    
    
    