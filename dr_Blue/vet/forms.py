from django import forms

from .models import PetOwner, Pet


class OwnerForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "address", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Tu nombre, perro","class": "holi"}
            )}

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "type", "owner"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "nombre de tu mascota","class": "holi"}
            )}