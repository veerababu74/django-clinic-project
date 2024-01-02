from django.db import models
from unittest.util import _MAX_LENGTH
# from django.models import Evangelized
# Create your models here.
from django.core import validators

class Patient(models.Model):
    lastname=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    age=models.IntegerField()


class ClinicData(models.Model):
    COMPONENT_NAMES=[('hw','hight/HIGHT'),('bp','Blood Presuer'),('hertrate','heart rate')]
    componentname=models.CharField(max_length=20, choices=COMPONENT_NAMES)
    componentval=models.CharField(max_length=20)
    mesureddatetime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)



