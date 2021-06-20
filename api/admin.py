from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Courier, Device

class CourierAdmin(admin.ModelAdmin):
    model = Courier
    list_display = ('user', 'get_email','company_token','created_at', 'updated_at')
    readonly_fields = ('created_at',)
    search_fields = ('company_token',)

    fieldsets = (
        (None, {
            'fields': ( 'user', 'company_token',)
        }),
    )

    def get_email(self, obj):
        if not obj.user:
            return ""
        return obj.user.email
    
    get_email.admin_order_field = 'user' # Allows column order sorting
    get_email.short_description = 'Courier email' # Renames column head

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super(CourierAdmin, self).get_queryset(request).select_related('user')


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = ('device_id','device_model', 'app', 'version', 'get_courier')
    search_fields = ('company_token','device_id', 'device_model')

    fieldsets = (
        (None, {
            'fields': ( 'courier','device_id', 'device_model', 'app', 'version')
        }),
    )

    def get_courier(self, obj):
        return obj.courier.company_token
    
    get_courier.admin_order_field = 'courier' # Allows column order sorting
    get_courier.short_description = 'Courier Company ID' # Renames column head

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super(DeviceAdmin, self).get_queryset(request).select_related('courier')

admin.site.register(Courier, CourierAdmin)
admin.site.register(Device, DeviceAdmin)