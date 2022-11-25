from rest_framework import serializers
from prueba.models import Persona

class AdminPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("id", "nombres", "apellidos", "correo")
        read_only = ("id", )