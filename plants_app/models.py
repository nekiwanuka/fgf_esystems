from django.db import models
from django.contrib.auth.models import User

# Choices for life_form field
LIFE_FORM_CHOICES = [
    ('forest', 'Forest'),
    ('meadow', 'Meadow'),
    ('climber', 'Climber'),
    ('grassland', 'Grassland'),
    ('herb', 'Herb'),
    ('shrub', 'Shrub'),
    ('tree', 'Tree'),
]

class Language(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    # General information
    botanical_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    region_in_Uganda = models.CharField(max_length=100, blank=True, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    life_form = models.CharField(max_length=100, choices=LIFE_FORM_CHOICES, null=True)
    
    #description is missing

     
    # Values and properties
    social_value = models.TextField()
    economical_value = models.TextField()
    cultural_value = models.TextField()
    other_value = models.TextField()
    
    # Multimedia
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    video = models.FileField(upload_to='plant_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='plant_audio/', blank=True, null=True)
    
    # Notes
    notes = models.TextField()
    contributor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=255) 
    
    # Associated names in different languages
    names = models.ManyToManyField(Language, through='PlantName', related_name='plant_names')

    def __str__(self):
        return f"Plant: {self.botanical_name}"

class PlantName(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Plant Name: {self.name} - Language: {self.language}"

class MedicinalPlant(models.Model):
    # Associated plant information
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, related_name='medicinal_info')
    
    # Medicinal information
    health_issues = models.TextField()
    part_used = models.CharField(max_length=100, blank=True, null=True)
    preparation_steps = models.TextField()
    dosage = models.CharField(max_length=100, blank=True, null=True)
    contraindications = models.TextField()
    shelf_life = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField()
    contributor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    
    # Associated names in different languages
    names = models.ManyToManyField(Language, through='MedicinalPlantName', related_name='medicinal_plant_names')

    def __str__(self):
        return f"Medicinal Info for Plant: {self.plant.botanical_name}"

class MedicinalPlantName(models.Model):
    medicinal_plant = models.ForeignKey(MedicinalPlant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Medicinal Plant Name: {self.name} - Language: {self.language}"
