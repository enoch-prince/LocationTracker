from django.contrib.auth.models import User
from .models import Courier, Device
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        read_only_fields = ('is_superuser', 'created_at')

class CourierSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Courier
        fields = ("user", "company_token", "created_at", "updated_at")
        read_only_fields = ('created_at', 'updated_at')


class DeviceSerializer(ModelSerializer):
    courier = CourierSerializer()
    
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')