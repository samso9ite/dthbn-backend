# Generated by Django 3.0.4 on 2020-04-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200409_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_professional',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_school',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
