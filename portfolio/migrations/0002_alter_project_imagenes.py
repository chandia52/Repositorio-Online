# Generated by Django 4.2 on 2023-06-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagenes',
            field=models.ImageField(upload_to='portfolio/images'),
        ),
    ]