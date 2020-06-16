from django.db import models

# Create your models here.


class Programacion_web(models.Model):
    unit1 = models.IntegerField("Unidad 1")
    unit2 = models.IntegerField("Unidad 2")
    unit3 = models.IntegerField("Unidad 3")

    def promedio(self):
        return (self.unit1+self.unit2+self.unit3)/3


class Soa(models.Model):
    unit1 = models.IntegerField("Unidad 1")
    unit2 = models.IntegerField("Unidad 2")
    unit3 = models.IntegerField("Unidad 3")

    def promedio(self):
        return (self.unit1+self.unit2+self.unit3)/3


class Alumno(models.Model):
    name = models.CharField("nombre", max_length=30)
    last_name = models.CharField("apellido", max_length=30)
    pweb = models.ForeignKey(Programacion_web, on_delete=models.CASCADE)
    arqui = models.ForeignKey(Soa, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)
