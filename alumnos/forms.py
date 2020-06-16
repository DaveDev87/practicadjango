from django import forms

from .models import Alumno, Soa, Programacion_web

    
    
class SoaForm(forms.ModelForm):
    class Meta:
        model = Soa
        fields = [
            "unit1",
            "unit2",
            "unit3"
        ]

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"
        
   