from django.urls import path, include
#from rest_framework import routers
#from .views import OwnersViewSet, PetsViewSet
from .views import ListOwnersAPIView,RetrieveOwnersAPIView,CreateOwnersAPIView,UpdateOwnersAPIView, DestroyOwnersAPIView
from .views import ListPetsAPIView,RetrievePetsAPIView,CreatePetsAPIView
from .views import CreateBranchOfficeAPIView,ListBranchOfficeAPIView

urlpatterns = [
    path("owners/",ListOwnersAPIView.as_view(), name= "list-owners"),
    path("owners/create/",CreateOwnersAPIView.as_view, name="create-owners"),
    path("owners/<int:pk>/update/",UpdateOwnersAPIView.as_view, name = "update-owners"),
    path("owners/<int:pk>/",RetrieveOwnersAPIView.as_view(),name="retrieve-owners"),
    path("owners/<int:pk>/destroy/",RetrieveOwnersAPIView.as_view(),name="destroy-owners"),

    path("pets/",ListPetsAPIView.as_view(), name= "list-pets"),
    path("pets/create/",CreatePetsAPIView.as_view, name="create-pets"),
    path("pets/<int:pk>/",RetrievePetsAPIView.as_view(),name="retrieve-pets"),

    path("branch/create/",CreateBranchOfficeAPIView.as_view(),name = "create-branch-office"),
    path("branch/",ListBranchOfficeAPIView.as_view(),name="list-branch")
]










#router = routers.DefaultRouter()
#router.register(r"owners", OwnersViewSet)
#router.register(r"pets",PetsViewSet)

#urlpatterns = [
#    path("", include(router.urls)),
    #path("/pets/",include(router.urls)),#<---
    #urls para pets y para petsdate
#]