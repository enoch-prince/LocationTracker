from tracker.models import Location
from tracker.serializers import LocationSerializer
from tracker.permissions import LocationAccessPermission, LocationEditPermission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings
from typing import Any, Dict
import json


class LocationView(ListCreateAPIView, LocationAccessPermission):
    permission_classes = [LocationAccessPermission]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationViewDetail(RetrieveUpdateDestroyAPIView, LocationEditPermission):
    permission_classes = [LocationAccessPermission]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class HomeView(TemplateView):
    template_name = "tracker/home.html"

class IndexView(PermissionRequiredMixin, TemplateView):
    permission_required = ('tracker.view_location',)
    permission_denied_message = "Only Admins can view this page!"
    template_name = "tracker/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["GOOGLE_MAPS_API_KEY"] = settings.GOOGLE_MAPS_API_KEY
        queryset = Location.objects.all()
        locations = [{"lat": float(loc.latitude), "lng": float(loc.longitude), "lbl": loc.device_id} for loc in queryset]
        context["locations"] = json.dumps(locations)
        return context