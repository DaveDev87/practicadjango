from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse

from .forms import AlumnoForm, SoaForm
from .models import Alumno

# Create your views here.


# def create_alumno(request):
#     context = {}
#     return render(request, "alumnos/alumno_create.html", context)


def create_alumno(request):
    form = AlumnoForm(request.POST or None)
    soa = SoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    if soa.is_valid():
        soa.save()

    context = {
        "form": form,
        "soa": soa
    }

    return render(request, "alumnos/alumno_create.html", context)


def index(request):
    alumno = Alumno.objects.all()
    context = {'alumno': alumno}
    return render(request, 'alumnos/index.html', context)
