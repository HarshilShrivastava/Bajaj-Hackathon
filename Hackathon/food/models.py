from django.db import models

# Create your models here.
class Food(models.Model):
    PID=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=255)
    Food_Group=models.CharField(max_length=255,null=True)
    Calories=models.PositiveIntegerField(null=True)
    Fat=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Protein =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Carbohydrate =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Sugars =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Fiber =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Cholesterol =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Saturated_Fats =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)