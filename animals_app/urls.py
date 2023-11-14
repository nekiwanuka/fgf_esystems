from django.urls import path
from .views import (
    CountEntriesAPIView,
    AnimalListCreateView,
    AnimalDetailView,
    AnimalClassificationListCreateView,
    AnimalClassificationDetailView,
    AnimalLocalNameListCreateView,
    AnimalLocalNameDetailView
)

urlpatterns = [
    path('api/count-entries/', CountEntriesAPIView.as_view(), name='count-entries'),

    path('api/animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('api/animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),

    path('api/animal-classifications/', AnimalClassificationListCreateView.as_view(), name='animal-classification-list-create'),
    path('api/animal-classifications/<int:pk>/', AnimalClassificationDetailView.as_view(), name='animal-classification-detail'),

    path('api/animal-local-names/', AnimalLocalNameListCreateView.as_view(), name='animal-local-name-list-create'),
    path('api/animal-local-names/<int:pk>/', AnimalLocalNameDetailView.as_view(), name='animal-local-name-detail'),
]
