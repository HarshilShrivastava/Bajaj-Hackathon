from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

CONDITION_CHOICES = (
    ('1','Underweight'),
    ('2', 'Normal'),
    ('3','Overweight'),
    ('4','Obesity'),
)
Goals_Choices=(
    (
        ('1','Extreme Loose Weight'),
        ('2','Minor Loose Weight'),
        ('3','Maintain Weight'),
        ('4','Weight gain'),
        ('5','Extreme Weight gain'),
    )
)
Activity_Choices=(
    (
        ('1','Sedentary'),
        ('2','Lightly Active'),
        ('3','Active'),
        ('4','Very Active'),

    )
)
Gender_CHOICES = (
    ('1','Male'),
    ('2', 'Female'),
    ('3','Transgender'),
)
class Profile(models.Model):
    User=models.OneToOneField(User , on_delete=models.CASCADE)
    Gender=models.CharField( max_length=1, choices=Gender_CHOICES)
    Age=models.PositiveIntegerField()
    Weight = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(258)],)
    Height =models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(210)],)
    Condition = models.CharField(max_length=1, choices=CONDITION_CHOICES)
    BMI=models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(35)],)
    Goals=models.CharField(max_length=1, choices=Goals_Choices)
    Activity=models.CharField(max_length=1, choices=Activity_Choices)
    DailyCalories=models.PositiveIntegerField()
    BMR=models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10000)],)