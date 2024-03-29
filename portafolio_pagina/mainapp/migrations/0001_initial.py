# Generated by Django 5.0.1 on 2024-02-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_imagen', models.CharField(max_length=50)),
                ('descripcion_imagen', models.CharField(max_length=300)),
                ('imagen', models.ImageField(null=True, upload_to='static/image_of_the_day')),
            ],
        ),
    ]
