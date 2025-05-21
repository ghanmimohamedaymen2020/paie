from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocieteViewSet, EmployeViewSet, BulletinPaieViewSet
from gestion_paie_app import views

router = DefaultRouter()
router.register(r'societes', SocieteViewSet)
router.register(r'employes', EmployeViewSet)
router.register(r'bulletins', BulletinPaieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.home, name='home'),

]