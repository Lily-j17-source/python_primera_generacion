from rest_framework import viewsets

from vet.models import PetOwner, Pet
from .serializers import OwnersSerializer, PetsSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class PetsViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo Pet.
    """
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsSerializer