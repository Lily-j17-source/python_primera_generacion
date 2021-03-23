from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView,ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import PetOwner
from .models import Pet
from .forms import OwnerForm, PetForm

# Create your views here.
class Owners(View):
    def get(self,request):
        owners = PetOwner.object.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))

#class OwnersList(TemplateView):
#    template_name = "vet/owners/list.html"
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        #print(context, "ESTO VIENE DEL PADRE (TEMPLATEVIEW)")
#        context["owners"] = PetOwner.objects.all()
#        #print(context, "ESTO LE AGREGAMOS NOSOTROS")
#        return context


class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class OwnersCreate(CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class OwnersUpdate(UpdateView):
    model=Pet
    form_class = PetForm
    template_name = "vet/owners/update.html"
    success_url = reverse_lazy("vet:owners_list")





#class Pets(View):
#    def get(self,request):
#        pets = Pet.object.all()
#        context = {"pets": pets}
#
#        template = loader.get_template("vet/owners/pets/petlist.html")
#        return HttpResponse(template.render(context, request))


#class PetsList(TemplateView):
#    template_name = "vet/pets/petlist.html"
#
#   def get_context_data(self,**kwargs):
#        context = super().get_context_data(**kwargs)
#
#        context["pets"] = Pet.objects.all()
#        return context


class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"


class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/petdetails.html"
    context_object_name = "pet"

class PetsCreate(CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    fields = ["name","type","owner"]
    success_url = reverse_lazy("vet:pets_list")

class PetsUpdate(UpdateView):
    model=Pet
    form_class = PetForm
    template_name = "vet/pets/update.html"
    success_url = reverse_lazy("vet:pets_list")