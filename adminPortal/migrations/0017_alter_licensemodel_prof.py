# Generated by Django 4.2.6 on 2024-03-18 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminPortal', '0016_delete_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensemodel',
            name='prof',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='license', to=settings.AUTH_USER_MODEL),
        ),
    ]