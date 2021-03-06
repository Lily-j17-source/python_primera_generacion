from django.urls import path
from .views import OwnersList, OwnersDetail, OwnersCreate, OwnersUpdate
from .views import PetsList, PetsDetail, PetsCreate, PetsUpdate
from .views import DatesCreate, DatesDetail

urlpatterns = [
    path("owners/", OwnersList.as_view(),name="owners_list"),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("owners/<int:pk>/", OwnersDetail.as_view(), name="owners_detail"),
    path("owners/<int:pk>/update/",OwnersUpdate.as_view(),name="owners_update"),
    #path("pets/",PetsList.as_view()),
    path("pets/", PetsList.as_view(),name="pets_list"),
    path("pets/<int:pk>/", PetsDetail.as_view(), name="pets_detail"),
    path("pets/add/", PetsCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/update/",PetsUpdate.as_view(),name="pets_update"),
    path("dates/add/", DatesCreate.as_view(), name="dates_create"),
    path("dates/details/",DatesDetail.as_view(),name="dates_detail"),
]