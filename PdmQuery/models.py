from django.db import models

# Create your models here.


class ICohm(models.Model):
    PartNumber = models.CharField(max_length=20)
    Description = models.CharField(max_length=40)
    OhmValue = models.PositiveIntegerField()
    Tolerance = models.DecimalField(max_digits=10, decimal_places=5)
    PackType = models.IntegerField()
    VoltageRating = models.IntegerField()  #额定电压
    Height_mm = models.DecimalField(max_digits=10, decimal_places=5)