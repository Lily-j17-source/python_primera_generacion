from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView,ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import PetOwner
from .models import Pet
from .models import PetDate

from .forms import OwnerForm, PetForm, DateForm
# Create your views here.
class OwnersList(LoginRequiredMixin,ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"
    login_url = reverse_lazy("login")


class OwnersDetail(LoginRequiredMixin,DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"
    login_url = reverse_lazy("login")

class OwnersCreate(LoginRequiredMixin,CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")

class OwnersUpdate(LoginRequiredMixin,UpdateView):
    model=Pet
    form_class = PetForm
    template_name = "vet/owners/update.html"
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")

#class Pets
#  ------------------

class PetsList(LoginRequiredMixin,ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"
    login_url = reverse_lazy("login")


class PetsDetail(LoginRequiredMixin,DetailView):
    model = Pet
    template_name = "vet/pets/petdetails.html"
    context_object_name = "pet"
    login_url = reverse_lazy("login")

class PetsCreate(LoginRequiredMixin,CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    fields = ["name","type","owner"]
    success_url = reverse_lazy("vet:pets_list")
    login_url = reverse_lazy("login")

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam]=self.request.GET[queryparam]
        return initial

class PetsUpdate(UpdateView):
    model=Pet
    form_class = PetForm
    template_name = "vet/pets/update.html"
    success_url = reverse_lazy("vet:pets_list")
    login_url = reverse_lazy("login")

#-----------DATES-----------------
class DatesCreate(LoginRequiredMixin,CreateView):
    model = PetDate
    template_name = "vet/dates/create.html"
    form_class = DateForm
    success_url = reverse_lazy("vet:dates_create")#<---
    login_url = reverse_lazy("login")

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam] = self.request.GET[queryparam]

        return initial

class DatesDetail(LoginRequiredMixin,DetailView):
    model = PetDate
    template_name = "vet/dates/details.html"
    context_object_name = "date"
    login_url = reverse_lazy("login")