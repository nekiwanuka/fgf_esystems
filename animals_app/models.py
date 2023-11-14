from django.db import models
from django.contrib.auth.models import User

class AnimalClassification(models.Model):
    kingdom_name = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    number_of_species = models.IntegerField(default=1, null=True)
    animal_class = models.CharField(max_length=250)
    order = models.CharField(max_length=250)

    def __str__(self):
        return self.animal_class

class Animal(models.Model):
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    areas_in_Uganda = models.CharField(max_length=250)
    animal_classifications = models.ForeignKey(AnimalClassification, on_delete=models.SET_NULL, null=True)
    known_values = models.CharField(max_length=250)
    value_details = models.CharField(max_length=250)
    unique_habitat = models.CharField(max_length=250)
    threats = models.TextField()
    notes = models.TextField()
    image = models.ImageField(upload_to='animal_images', null=True, blank=True)
    video = models.FileField(upload_to='animal_videos', null=True, blank=True)
    audio = models.FileField(upload_to='animal_audios', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.TextField()
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_name} ({self.scientific_name})"

class AnimalLocalName(models.Model):
    local_name = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.local_name} ({self.language}) for {self.animal.english_name} ({self.animal.scientific_name})"
    