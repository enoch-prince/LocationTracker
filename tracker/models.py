from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Location(models.Model):
    latitude = models.DecimalField(_("Latitude"),
                max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(_("Longitude"),
                max_digits=15, decimal_places=10, null=True, blank=True)
    device_id = models.CharField(_("Device Serial Number"), max_length=80, unique=True)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now_add=True)
