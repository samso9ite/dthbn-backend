# Generated by Django 4.2.6 on 2024-06-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profPortal', '0008_licensereceipt_remita_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensereceipt',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
