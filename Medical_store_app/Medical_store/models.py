from django.db import models

# Create your models here.
class Medicine(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    company=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.FloatField()
    mfg_date=models.DateField()
    exp_date=models.DateField()