from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomUserPermission(BasePermission):
    message = "Editing someone else data is restricted to the owner and admin only"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.email == request.user.email