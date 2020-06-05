# Generated by Django 3.0.6 on 2020-06-04 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_food_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailablityLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AvailablityZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vitamins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodNutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Unitconversion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('Calories', models.PositiveIntegerField(null=True)),
                ('Lactose_Intolerance', models.BooleanField(default=False)),
                ('Fat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Protein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Carbohydrate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Sugars', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Fiber', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Cholesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Saturated_Fats', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Food/')),
                ('Availablity', models.ManyToManyField(to='food.AvailablityZone')),
                ('AvailablityTier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.AvailablityLevel')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Category')),
                ('Food_Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.FoodGroup')),
                ('Problems_Can_Solve', models.ManyToManyField(to='food.Problem')),
                ('Processing_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Processing')),
                ('Vitamins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Vitamins')),
            ],
        ),
    ]
