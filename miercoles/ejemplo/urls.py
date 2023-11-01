from django.http import HttpResponse

from django.contrib import admin
from django.urls import path
from .views import Alumnos, Profesores
urlpatterns = [
    path('alumnos/<str:nombre>/', Alumnos.as_view(), name="alumnos"),
    path("profesores/<str:nombre>/<str:alumnos>", Profesores.as_view(), name="profesores")
]