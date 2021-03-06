# Generated by Django 3.0.6 on 2020-05-13 11:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=50)),
                ('Weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(258)])),
                ('Height', models.FloatField(validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(210)])),
                ('Condition', models.CharField(choices=[('1', 'Underweight'), ('2', 'Normal'), ('3', 'Overweight'), ('4', 'Obesity')], max_length=1)),
                ('BMI', models.FloatField(validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(35)])),
                ('Goals', models.CharField(choices=[('1', 'Loose Fat'), ('2', 'Loose Fat and gain muscle'), ('3', 'gain muscle'), ('4', 'Shreing')], max_length=1)),
                ('Activity', models.CharField(choices=[('1', 'Sedentary'), ('2', 'Lightly Active'), ('3', 'Active'), ('4', 'Very Active')], max_length=1)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
