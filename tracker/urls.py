from django.urls import path
from .views import HomeView, LocationView, LocationViewDetail, IndexView

app_name = 'tracker'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('tracker/', IndexView.as_view(), name='index'),
    path('tracker/api/location', LocationView.as_view()),
    path('tracker/api/location/<int:pk>', LocationViewDetail.as_view())
]


