from django.shortcuts import render
from django.views import View
# Create your views here.
class Agregar(View):
    def get(self, request, nombre):
        with open("registros.txt", "a") as file:
            file.write(nombre + ",")
            file.close()
        return render(request, "agregar.html",{
            "nombre": nombre,
        })

class Eliminar(View):
    def get(self, request, nombre):
        with open("registros.txt", "r") as file:
            string_crudo = file.read()
            file.close()
        with open("registros.txt", "w") as file:
            file.write(string_crudo.replace(nombre + ",", ""))
            file.close()
        return render(request, "eliminar.html", {
            "nombre": nombre
        })

class Entregar(View):
    def get(self, request):
        with open("registros.txt", "r") as file:
            string_crudo = file.read()
            file.close()
        lista = string_crudo.split(",")
        return render(request, "entregar.html", {
            "lista": lista,
        })