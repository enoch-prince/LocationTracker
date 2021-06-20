from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Courier(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, null=True, blank=True)
    company_token = models.CharField(_("Company Token"), max_length=150, unique=True)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now_add=True)

    def __str__(self) -> str:
        if self.user:
            return self.user.username
        return self.company_token

class Device(models.Model):
    courier = models.ForeignKey("Courier", verbose_name=_("Courier"), on_delete=models.CASCADE)
    device_id = models.CharField(_("Device Serial Number"), max_length=80, unique=True)
    device_model = models.CharField(_("Device Model"), max_length=50)
    app = models.CharField(_("Registration App Used"), max_length=50)
    version = models.CharField(_("App Version"), max_length=50)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now_add=True)
    