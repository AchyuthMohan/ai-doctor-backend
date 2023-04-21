from rest_framework import serializers
from .models import(User,Medicine,UserDetail,Doctor,MedicinePurchase,Book_appointment)
from rest_framework.permissions import (IsAuthenticated)

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class MedicineSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Medicine
        fields="__all__"

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetail
        fields="__all__"

class DoctorSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Doctor
        fields='__all__'
class MedicinePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicinePurchase
        fields='__all__'

class BookAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book_appointment
        fields='__all__'