# Generated by Django 3.0.4 on 2020-04-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexlimit',
            name='used_limit',
            field=models.IntegerField(),
        ),
    ]
