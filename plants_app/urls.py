from django.urls import path
from .views import (
    MedicinalPlantListView,
    MedicinalPlantDetailView,
    PlantListView,
    PlantDetailView,
    CalculateMedicinalPlantsCount,
    CalculatePlantsCount
)

urlpatterns = [
    path('api/medicinal-plants/', MedicinalPlantListView.as_view(), name='medicinal-plant-list'),
    path('api/medicinal-plants/<int:pk>/', MedicinalPlantDetailView.as_view(), name='medicinal-plant-detail'),
    path('api/plants/', PlantListView.as_view(), name='plant-list'),
    path('api/plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('api/calculate-medicinal-plants-count/', CalculateMedicinalPlantsCount.as_view(), name='calculate-medicinal-plants-count'),
    path('api/calculate-plants-count/', CalculatePlantsCount.as_view(), name='calculate-plants-count'),
    # ... other URL patterns ...
    path('api/plant_images/', PlantListView.as_view(), name='plant-list'), #create view for images
]
