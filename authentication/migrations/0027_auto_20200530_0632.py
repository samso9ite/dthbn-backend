# Generated by Django 3.0.4 on 2020-05-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_professionalcode_cadre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
