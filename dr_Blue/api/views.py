from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate

from .serializers import OwnersListSerializer, OwnersSerializer
from .serializers import PetsListSerializer, PetsSerializer
#from .serializers import OwnersSerializer, PetsSerializer

# Create your views here.

class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset= PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset= PetOwner.objects.all()
    serializers_class = OwnersSerializer

#-------PETS------generic class-------
class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    queryset= Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer







#Vistas por viewset-------------------------------------------------------
#class OwnersViewSet(viewsets.ModelViewSet):
 #   """
  #  ViewSet del modelo PetOwners.
   # """
#    queryset = PetOwner.objects.all()
 #   serializer_class = OwnersSerializer

#class PetsViewSet(viewsets.ModelViewSet):
 #   """
  #  ViewSet del modelo Pet.
   # """
  #  queryset = Pet.objects.all().order_by("created_at")
  #  serializer_class = PetsSerializer