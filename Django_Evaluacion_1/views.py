from django.conf import settings
import os 
from django.http import HttpResponse
from django.template import Template, Context



class Persona(object):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

def usuario(request):
    template_path = os.path.join(settings.BASE_DIR, 'plantillas/templatesWeb/usuario.html')
    with open(template_path, 'r') as doc_externo:
        plantilla = Template(doc_externo.read())

    persona1 = Persona("21", "Manuel Huenubil", "ManuelHuenubil@hotmail.com")
    cont = Context({"id_persona": persona1.id, "nom_persona": persona1.nombre, "email_persona": persona1.email})
    docu = plantilla.render(cont)
    return HttpResponse(docu)




