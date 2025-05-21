from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Societe, Employe, BulletinPaie
from .serializers import SocieteSerializer, EmployeSerializer, BulletinPaieSerializer
from .calcul_paie import calculer_paie

class SocieteViewSet(viewsets.ModelViewSet):
    queryset = Societe.objects.all()
    serializer_class = SocieteSerializer

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class BulletinPaieViewSet(viewsets.ModelViewSet):
    queryset = BulletinPaie.objects.all()
    serializer_class = BulletinPaieSerializer

    def create(self, request, *args, **kwargs):
        employe_id = request.data.get('employe')
        mois = int(request.data.get('mois'))
        annee = int(request.data.get('annee'))
        try:
            employe = Employe.objects.get(pk=employe_id)
            bulletin = calculer_paie(employe, mois, annee)
            serializer = self.get_serializer(bulletin)
            return Response(serializer.data)
        except Employe.DoesNotExist:
            return Response({'error': 'Employé non trouvé'}, status=404)
def home(request):
   return render(request, 'gestion_paie_app/home.html')