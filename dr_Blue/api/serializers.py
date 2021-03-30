from rest_framework import serializers

from vet.models import PetOwner,Pet,PetDate,BranchOffice

# Serializers define the API representation.

class OwnersListSerializer(serializers.ModelSerializer):#*se encarga del listado de nuestra informacion
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name"]


class OwnersSerializer(serializers.ModelSerializer):#*
    class Meta:
        model=PetOwner
        fields = "__all__"


#------------------PETS---generic class
class PetsListSerializer(serializers.ModelSerializer):#solo 3 campos*
    class Meta:
        model = Pet
        fields = ["id","name"]

class PetOwnerSerializer(serializers.ModelSerializer):#*
    owner = OwnersListSerializer()
    class Meta:
        model = Pet
        fields = ["id","name","type","created_at","owner"]


class OwnerPetsSerializer(serializers.ModelSerializer):#***new
    pets = PetsListSerializer(many = True)
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name","email","phone","address","created_at","pets"]
#class PetsSerializer(serializers.ModelSerializer):#todos los campos
 #   class Meta:
  #      model = Pet
   #     fields = "__all__"

#-----------PetDate----------------------->
class PetDatesListSerializer(serializers.ModelSerializer):#solo algunos campos
    class Meta:
        model = PetDate
        fields = ["id","type","datetime","branch_office"]

class PetDatesSerializer(serializers.ModelSerializer):#todos los campos(datetime, type,pet,branch_office)
    class Meta:
        model = PetDate
        fields = "__all__"

#-------------Branch Office--------------->
class BranchOfficeListSerializer(serializers.ModelSerializer):#list
    class Meta:
        model = BranchOffice
        fields =["alias","zip_code","address","phone"]

class BranchOfficeSerializer(serializers.ModelSerializer):#serializer all)
    class Meta:
        model = BranchOffice
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
        