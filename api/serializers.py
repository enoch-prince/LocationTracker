from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from .models import Courier, Device
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from datetime import datetime

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
    
    def create(self, validated_data):
        # pop out the dict to create user field for courier
        user_data = validated_data.pop('user')
        # check if user already exists
        queryset = User.objects.filter(Q(id=user_data.id) | Q(username=user_data.username))
        if queryset.exists():
            user_obj = queryset.first()
        else:
            # create user first
            user_obj = User.objects.create(**user_data)
        # create the courier 
        courier = Courier.objects.create(user=user_obj, **validated_data)
        return courier
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.company_token = validated_data.get("company_token", instance.company_token)
        instance.updated_at = datetime.now().replace(microsecond=0)
        instance.save(update_fields=['user', 'company_token', 'updated_at'])
        return instance
        


class DeviceSerializer(ModelSerializer):

    courier_id = serializers.CharField(source='courier.id')
    
    class Meta:
        model = Device
        fields = ('id','courier_id', 'device_id', 'device_model', 'app', 'version', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
    
    def create(self, validated_data):
        print(validated_data)
        courier_data = validated_data.pop('courier')
        courier = Courier.objects.filter(id=courier_data.get('id'))
        if not courier.exists():
            return None
        device = Device.objects.create(courier=courier.first(), **validated_data)
        return device
    
    def update(self, instance, validated_data):
        courier_id = validated_data.get('courier').get('id')
        if not courier_id:
            return None
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.device_model = validated_data.get('device_model', instance.device_model)
        instance.app = validated_data.get('app', instance.app)
        instance.version = validated_data.get('version', instance.version)
        instance.updated_at = datetime.now().replace(microsecond=0)
        instance.save(update_fields=['device_id', 'device_model', 'app', 'version', 'updated_at'])
        return instance