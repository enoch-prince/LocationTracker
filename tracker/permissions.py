from rest_framework.permissions import BasePermission, SAFE_METHODS


class LocationAccessPermission(BasePermission):
    message = "Editing someone else data is restricted to the owner and admin only"

    def has_permission(self, request, view):
        print({"request": request.data.items()})
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return True

class LocationEditPermission(BasePermission):
    message = "Editing someone else data is restricted to the owner and admin only"

    def has_permission(self, request, view):
        print({"request": request.data.items()})
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        #print({"obj": dir(obj)})
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.device_id == request.data.get('device_id')