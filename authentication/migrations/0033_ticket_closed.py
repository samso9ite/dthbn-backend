# Generated by Django 3.0.4 on 2020-06-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0032_auto_20200603_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
