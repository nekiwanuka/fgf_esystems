from django.urls import path, re_path, include
from django.contrib import admin


# Import drf-yasg components
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create an OpenAPI schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Name",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

# Define your urlpatterns
urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path(
        "api/schema/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("", include("animals_app.urls"), name="animals"),
    path("", include("cultures_app.urls"), name="cultures"),
    path("", include("plants_app.urls"), name="plants"),
    
]
