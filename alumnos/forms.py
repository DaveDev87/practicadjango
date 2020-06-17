from django import forms

from .models import Alumno, Soa, Programacion_web

    
    

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"
        
   