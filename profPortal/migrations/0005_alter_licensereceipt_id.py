# Generated by Django 4.2.6 on 2024-06-30 21:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profPortal', '0004_alter_professional_profuser_licensereceipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensereceipt',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
