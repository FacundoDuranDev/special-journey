from django.urls import path
from .views import Agregar, Eliminar, Entregar

urlpatterns = [
    path('agregar/<str:nombre>', Agregar.as_view(), name='agregar'),
    path('eliminar/<str:nombre>', Eliminar.as_view(), name='eliminar'),
    path('entregar/', Entregar.as_view(), name='entregar'),
]
