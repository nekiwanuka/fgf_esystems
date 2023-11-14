from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Plant, MedicinalPlant
from .serializers import PlantSerializer, MedicinalPlantSerializer
from .filters import PlantFilter, MedicinalPlantFilter

# ... Existing imports ...

class MedicinalPlantListView(generics.ListCreateAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MedicinalPlantFilter
    search_fields = ['health_issues', 'part_used']

class MedicinalPlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer

class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = PlantFilter
    search_fields = ['region_in_Uganda', 'habitat']

    

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    #PK added to enable get by ID on front end
    """ def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PlantSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  """
    
    """ def get(self, request, *args, **kwargs):
        response = Response({'key': 'value'})
        response['Access-Control-Allow-Origin'] = 'http://localhost:5173'  
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response """

class CalculateMedicinalPlantsCount(APIView):
    serializer_class = MedicinalPlantSerializer

    def get(self, request, *args, **kwargs):
        medicinal_plants_count = MedicinalPlant.objects.count()
        return Response({'medicinal_plants_count': medicinal_plants_count}, status=status.HTTP_200_OK)

class CalculatePlantsCount(APIView):
    serializer_class = PlantSerializer

    def get(self, request, *args, **kwargs):
        plants_count = Plant.objects.count()
        return Response({'plants_count': plants_count}, status=status.HTTP_200_OK)
