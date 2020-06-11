from rest_framework.permissions import SAFE_METHODS, BasePermission


class SafeMethodsOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj=None):
        return request.method in SAFE_METHODS


class AdminOrUserCanEdit(BasePermission):
    def has_permission(self, request, view):
        """All users can list or view."""
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj=None):
        """Only the user can modify existing instances."""
        is_safe = request.method in SAFE_METHODS

        try:
            is_user = request.user == obj.user
        except AttributeError:
            is_user = False

        return is_safe or is_user or request.user.is_superuser
