from rest_framework.fields import ReadOnlyField
from .models import Location
from rest_framework.serializers import ModelSerializer

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')