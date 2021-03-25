from django.urls import path, include
from rest_framework import routers
from .views import OwnersViewSet, PetsViewSet

router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)
router.register(r"pets",PetsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #path("/pets/",include(router.urls)),#<---
    #urls para pets y para petsdate
]