# Generated by Django 3.0.6 on 2020-05-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20200519_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Food/'),
        ),
    ]