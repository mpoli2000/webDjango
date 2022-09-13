from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self, name):
    return HttpResponse(f'Hola soy {name}')

def homePage(self):
    data = {'nombre':'Martin','apellido':'Poli'}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    #planilla = loader.get_template('cursos.html')
    #documento = planilla.render()
    curso = Curso(nombre='UX/UI', camada=1234)
    curso.save()
    documento = f'Curso: {curso.nombre}, camada: {curso.camada}'
    return HttpResponse(documento)
