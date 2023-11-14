from rest_framework import permissions

class CreateAuthenticatedPermission(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to create objects.
    """

    def has_permission(self, request, view):
        # Allow GET requests (list view) for all users
        if request.method == 'GET':
            return True

        # Check if the user is authenticated for non-GET requests
        return request.user and request.user.is_authenticated
