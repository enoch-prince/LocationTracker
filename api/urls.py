from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('device', DeviceView.as_view()),
    path('device/<int:pk>', DeviceViewDetail.as_view()),
    path('courier', CourierView.as_view()),
    path('courier/<int:pk>', CourierViewDetail.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserViewDetail.as_view())
]
