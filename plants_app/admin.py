from django.contrib import admin
from .models import MedicinalPlant, Plant, PlantName, Language

# Register the models with the custom admin classes
admin.site.register(MedicinalPlant)
admin.site.register(Plant)
admin.site.register(PlantName)
admin.site.register(Language)
