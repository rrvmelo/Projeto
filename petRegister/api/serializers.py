from rest_framework import serializers
from petRegister import models

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetRegistro
        fields = '__all__'

class PetMensagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MensagemPet
        fields = '__all__'