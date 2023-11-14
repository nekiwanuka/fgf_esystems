# utils/authentication_extensions.py

from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.permissions import BasePermission

class AuthTokenAuthenticationExtension(SwaggerAutoSchema):
    def get_security(self):
        return [{'authToken': []}]
