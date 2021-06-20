from tracker.models import Location
from django.conf import settings
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'latitude', 'longitude', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('device_id',)

    fieldsets = (
        (None, {
            'fields': ( 'device_id', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_map.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_map.js',
            )

admin.site.register(Location, LocationAdmin)