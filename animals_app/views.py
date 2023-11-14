from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, AnimalClassification, AnimalLocalName
from .serializers import AnimalSerializer, AnimalClassificationSerializer, AnimalLocalNameSerializer, CountEntriesSerializer
from django.db.models import Count

class CountEntriesAPIView(APIView):
    serializer_class = CountEntriesSerializer  # Specify the serializer class

    def get(self, request):
        # Count the total number of entries for animals
        total_animal_count = Animal.objects.count()

        # Count the total number of entries for animal classifications
        total_classification_count = AnimalClassification.objects.count()

        # Count the total number of animal species
        total_species_count = AnimalClassification.objects.aggregate(total_species_count=Count('species', distinct=True))['total_species_count']

        # Create a response data dictionary
        response_data = {
            'total_animal_count': total_animal_count,
            'total_classification_count': total_classification_count,
            'total_species_count': total_species_count
        }

        # Serialize the response data
        serializer = self.serializer_class(response_data)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    #PK added to enable get by ID on front end
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = AnimalSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalSerializer


class AnimalClassificationListCreateView(generics.ListCreateAPIView):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer


class AnimalClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalClassification.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalClassificationSerializer


class AnimalLocalNameListCreateView(generics.ListCreateAPIView):
    queryset = AnimalLocalName.objects.all()
    serializer_class = AnimalLocalNameSerializer


class AnimalLocalNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalLocalName.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalLocalNameSerializer
