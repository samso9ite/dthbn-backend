# Generated by Django 3.0.4 on 2021-03-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0004_auto_20210324_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexing',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
