from rest_framework import serializers

from vet.models import PetOwner,Pet,PetDate

# Serializers define the API representation.

class OwnersListSerializer(serializers.ModelSerializer):#se encarga del listado de nuestra informacion
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name"]


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=PetOwner
        fields = "__all__"

#------------------PETS---generic class
class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name","type"]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"





#class OwnersSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
 #       model = PetOwner
  #      fields = [
   #         "id",
    #        "first_name",
     #       "last_name",
      #      "email",
       #     "phone",
#            "address",
 #           "created_at",
  #      ]


#class PetsSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Pet
   #     fields = [
    #        "id","name","type",
     #       ]
        