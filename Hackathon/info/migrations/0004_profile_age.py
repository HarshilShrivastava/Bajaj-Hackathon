# Generated by Django 3.0.2 on 2020-05-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_profile_dailycalories'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Age',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]
