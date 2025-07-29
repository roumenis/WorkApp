from django.db import models

# Create your models here.

class ExcelData(models.Model):
    kurz = models.CharField(max_length=5) # 12/810
    linka = models.DecimalField(max_digits=5, decimal_places=2) # 13 ()
    prijezd = models.CharField(max_length=5) # 10:00
    odjezd = models.CharField(max_length=5) # 10:05
    kolej = models.CharField(max_length=1) # 0,1,2...
    
    