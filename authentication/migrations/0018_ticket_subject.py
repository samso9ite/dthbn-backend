# Generated by Django 3.0.4 on 2020-05-15 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20200515_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
