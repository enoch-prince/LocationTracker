from django.contrib.auth.models import User
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from api.permissions import CustomUserPermission
from api.serializers import CourierSerializer, DeviceSerializer, UserSerializer
from api.models import Courier, Device
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DeviceView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class CourierView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class CourierViewDetail(RetrieveUpdateDestroyAPIView, CustomUserPermission):
    permission_classes = [CustomUserPermission]
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class UserView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewDetail(RetrieveUpdateDestroyAPIView, CustomUserPermission):
    permission_classes = [CustomUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer