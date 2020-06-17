from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse

from .forms import AlumnoForm
from .models import Alumno, Soa, Programacion_web

# Create your views here.


# def create_alumno(request):
#     data = request.POST

#     soaInit = Soa(unit1=data.get("a_u1"), unit2=data.get(
#         "a_u2"), unit3=data.get("a_u3"))

#     soaInit.save()
#     print("test",soaInit)

#     pwebInit = Programacion_web(unit1=data.get(
#         "p_u1"), unit2=data.get("p_u2"), unit3=data.get("p_u3"))

#     form = Alumno(name=data.get("name"), last_name=data.get(
#         "last_name"), pweb=pwebInit, arqui=soaInit)


#     context = {"form": form}
#     return render(request, "alumnos/alumno_create.html", context)


def create_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }

    return render(request, "alumnos/alumno_create.html", context)


def index(request):
    alumno = Alumno.objects.all()
    context = {'alumno': alumno}
    return render(request, 'alumnos/index.html', context)
