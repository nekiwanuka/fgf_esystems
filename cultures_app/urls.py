from django.urls import path
from .views import (
    ClanListView,
    ClanDetailView,
    CulturalKingdomListView,
    CulturalKingdomDetailView,
    EthnicityListView,
    EthnicityDetailView,
    EthnicGroupListView,
    EthnicGroupDetailView,

)

urlpatterns = [
    
    #path('api/cultures/', views.CulturalIdentityListCreateView.as_view(), name='culture-list-create'),
    #path('cultures/<int:pk>/', views.CulturalIdentityDetailView.as_view()),
    
    path('api/cultures/clans/', ClanListView.as_view()),
    path('api/cultures/clans/<int:pk>/', ClanDetailView.as_view()),
    
    path('api/cultures/cultural_kingdom/', CulturalKingdomListView.as_view()),
    path('api/cultures/cultural_kingdom/<int:pk>/', CulturalKingdomDetailView.as_view()),
    
    path('api/cultures/ethnicities/', EthnicityListView.as_view()),
    path('api/cultures/ethnicities/<int:pk>/', EthnicityDetailView.as_view()),
    
    path('api/cultures/', EthnicGroupListView.as_view(), name='culture-list'),
    path('api/cultures/<int:pk>/', EthnicGroupDetailView.as_view(), name='plant-detail'),
     
]

