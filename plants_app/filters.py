import django_filters
from .models import Plant, MedicinalPlant

class PlantFilter(django_filters.FilterSet):
    class Meta:
        model = Plant
        fields = {
            'region_in_Uganda': ['exact', 'icontains'],
            'habitat': ['exact', 'icontains'],
            'life_form': ['exact'],
            # Add more fields for filtering as needed
        }

class MedicinalPlantFilter(django_filters.FilterSet):
    class Meta:
        model = MedicinalPlant
        fields = {
            'health_issues': ['icontains'],
            'part_used': ['exact', 'icontains'],
            # Add more fields for filtering as needed
        }
