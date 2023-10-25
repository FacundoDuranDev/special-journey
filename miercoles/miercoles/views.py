from django.views import View
from django.http import HttpResponse

import random
import string
# "sys" es uno de los modulos mas importantes
# porque nos va a permitir interactuar con el sistema (system)
# también existe el modulo "os" que te permite interactuar con
# el sistema operativo (apagar la pc, leer un archivo, etc...)

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for number in range(longitud))
    return contraseña

class MiVista(View):
    def get(self,request):
        contraseña = generar_contraseña(16)
        return HttpResponse(contraseña)
