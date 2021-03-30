from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate, BranchOffice

from .serializers import OwnersListSerializer, OwnersSerializer,OwnerPetsSerializer
from .serializers import PetsListSerializer,PetOwnerSerializer
from .serializers import BranchOfficeListSerializer,BranchOfficeSerializer
from .serializers import PetDatesListSerializer, PetDatesSerializer
#from .serializers import OwnersSerializer, PetsSerializer

# Create your views here.

class ListOwnersAPIView(generics.ListAPIView):#muestra todos los elementos del modelo, todas los campos
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer #*

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset= PetOwner.objects.all()
    serializer_class = OwnersSerializer #*

class RetrieveOwnersAPIView(generics.RetrieveAPIView):#va por un elemento en especifico
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer #*

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer #*

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset= PetOwner.objects.all()
    serializers_class = OwnersSerializer #*

#-------PETS------generic class-------
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer #*

class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsListSerializer #*

#class CreatePetsAPIView(generics.CreateAPIView):
#    queryset= Pet.objects.all()
#    serializer_class = PetsSerializer

class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer #*
#-------------Branch office
class CreateBranchOfficeAPIView(generics.CreateAPIView):
    queryset= BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

class ListBranchOfficeAPIView(generics.ListAPIView):
    queryset = BranchOffice.objects.all().order_by("created_at")
    serializer_class = BranchOfficeListSerializer

class RetrieveBranchOfficeAPIView(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer
#-----------PetDate
class CreatePetDateAPIView(generics.CreateAPIView):
    queryset= PetDate.objects.all()
    serializer_class = PetDatesSerializer

class ListPetDateAPIView(generics.ListAPIView):
    queryset = PetDate.objects.all().order_by("created_at")
    serializer_class = PetDatesListSerializer





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