from rest_framework import serializers
from .models import Animal, AnimalClassification, AnimalLocalName

class AnimalLocalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocalName
        fields = '__all__'

class AnimalClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClassification
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    local_names = AnimalLocalNameSerializer(many=True, read_only=True)
    animal_classifications = AnimalClassificationSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = [
            'id', 'english_name', 'scientific_name', 'description', 'areas_in_Uganda',
            'known_values', 'value_details', 'unique_habitat', 'threats', 'notes',
            'image', 'video', 'audio', 'contributor_name', 'citation', 'date_entered',
            'local_names', 'animal_classifications'
        ]


class CountEntriesSerializer(serializers.Serializer):
    total_animal_count = serializers.IntegerField()
    total_classification_count = serializers.IntegerField()
    total_species_count = serializers.IntegerField()