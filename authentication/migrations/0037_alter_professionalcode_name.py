# Generated by Django 4.2.6 on 2024-03-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0036_professionalcode_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalcode',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
