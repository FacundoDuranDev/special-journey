from django.shortcuts import render
from django.views import View
# Create your views here.
class Alumnos(View):
    def get(self,request, nombre):
        return render(request, "alumnos.html", {
            "nombre": nombre,
        })
    
class Profesores(View):
    def get(self,request, nombre, alumnos):
        alumnos = alumnos.split(",")
        return render(request, "profesores.html", {
            "nombre": nombre,
            "alumnos": alumnos,
        })
