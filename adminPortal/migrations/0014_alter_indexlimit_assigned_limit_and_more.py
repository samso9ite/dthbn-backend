# Generated by Django 4.2.6 on 2023-12-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0013_closeexamregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexlimit',
            name='assigned_limit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='indexlimit',
            name='school',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='indexlimit',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
