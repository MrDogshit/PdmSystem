from django.db import models

# Create your models here.

class ICohm(models.Model):
    PartNumber = models.BigIntegerField()
    Description = models.CharField(max_length=40)
    OhmValue = models.PositiveIntegerField()
    Tolerance = models.FloatField()
    PackType = models.IntegerField()
    VoltageRating = models.IntegerField()  #额定电压
    Height_mm = models.FloatField()