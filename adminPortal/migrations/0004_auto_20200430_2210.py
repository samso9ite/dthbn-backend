# Generated by Django 3.0.4 on 2020-04-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0003_restrictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexlimit',
            name='assigned_limit',
            field=models.CharField(max_length=40),
        ),
    ]
