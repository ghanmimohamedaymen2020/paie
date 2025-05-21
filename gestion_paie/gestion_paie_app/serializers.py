from rest_framework import serializers
from .models import Societe, Employe, BulletinPaie

class SocieteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Societe
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    societe = SocieteSerializer(read_only=True)

    class Meta:
        model = Employe
        fields = '__all__'

class BulletinPaieSerializer(serializers.ModelSerializer):
    employe = EmployeSerializer(read_only=True)

    class Meta:
        model = BulletinPaie
        fields = '__all__'