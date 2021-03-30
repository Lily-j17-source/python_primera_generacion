from django.urls import path, include
#from rest_framework import routers
#from .views import OwnersViewSet, PetsViewSet
from .views import ListOwnersAPIView,RetrieveOwnersAPIView,CreateOwnersAPIView,UpdateOwnersAPIView
from .views import DestroyOwnersAPIView,RetrieveOwnerPetsAPIView,ListPetsAPIView, RetrievePetsOwnerAPIView

#from .views import RetrievePetsAPIView,CreatePetsAPIView

from .views import CreateBranchOfficeAPIView, ListBranchOfficeAPIView, RetrieveBranchOfficeAPIView
from .views import CreatePetDateAPIView, ListPetDateAPIView

urlpatterns = [
    path("owners/",ListOwnersAPIView.as_view(), name= "list-owners"),
    path("owners/create/",CreateOwnersAPIView.as_view, name="create-owners"),
    path("owners/<int:pk>/update/",UpdateOwnersAPIView.as_view, name = "update-owners"),
    path("owners/<int:pk>/",RetrieveOwnersAPIView.as_view(),name="retrieve-owners"),
    path("owners/<int:pk>/destroy/",RetrieveOwnersAPIView.as_view(),name="destroy-owners"),

    path("owners/<int:pk>/pets/",RetrieveOwnerPetsAPIView.as_view(),name="retrieve-owner-pets"),
    path("pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(), name="retrieve-pets-owner"),

    path("pets/",ListPetsAPIView.as_view(), name= "list-pets"),
    #path("pets/create/",CreatePetsAPIView.as_view, name="create-pets"),
    #path("pets/<int:pk>/",RetrievePetsAPIView.as_view(),name="retrieve-pets"),

    path("branch/create/",CreateBranchOfficeAPIView.as_view(),name="create-branch-office"),
    path("branch/",ListBranchOfficeAPIView.as_view(),name="list-branch"),
    path("branch/<int:pk>/",RetrieveBranchOfficeAPIView.as_view(), name = "retrieve-branch"),

    path("petsDates/",ListPetDateAPIView.as_view(),name="list-petDates"),
    path("petsDates/create/",CreatePetDateAPIView.as_view(),name="create-petsDate")  
]










#router = routers.DefaultRouter()
#router.register(r"owners", OwnersViewSet)
#router.register(r"pets",PetsViewSet)

#urlpatterns = [
#    path("", include(router.urls)),
    #path("/pets/",include(router.urls)),#<---
    #urls para pets y para petsdate
#]