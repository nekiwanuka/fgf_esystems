from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from cultures_app.models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from django.contrib.auth import logout
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.decorators import login_required





# Create your views here.
class ClanListView(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["clan_name"]


class ClanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clan.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class CulturalKingdomListView(generics.ListCreateAPIView):
    queryset = CulturalKingdom.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalKingdomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnicity_name"]


class CulturalKingdomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CulturalKingdom.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalKingdomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class EthnicityListView(generics.ListCreateAPIView):
    queryset = Ethnicity.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnicity_name"]


class EthnicityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ethnicity.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

#Not being used
class CulturalIdentityListCreateView(generics.ListCreateAPIView):
    queryset = CulturalIdentity.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] ---PK comment
    serializer_class = CulturalIdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]

    """ #PK added to enable get by ID on front end
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CulturalIdentitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) """

    
#Not being used  
class CulturalIdentityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CulturalIdentity.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalIdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class EthnicGroupListView(generics.ListCreateAPIView):
    queryset = EthnicGroup.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]
    #PK added to enable get by ID on front end
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = EthnicGroup(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class EthnicGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EthnicGroup.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicGroupSerializer
    #filter_backends = [DjangoFilterBackend, filters.SearchFilter]
