# filepath: /c:/Users/om/Desktop/aissmsioit/webapp/firstapp/models.py
from django.db import models

class Aissm(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.CharField(max_length=10)
    region = models.CharField(max_length=20)
    charges = models.FloatField()

    def __str__(self):
        return f"{self.age}, {self.sex}, {self.bmi}, {self.children}, {self.smoker}, {self.region}, {self.charges}"