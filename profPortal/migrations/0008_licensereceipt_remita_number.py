# Generated by Django 4.2.6 on 2024-06-30 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profPortal', '0007_alter_licensereceipt_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='licensereceipt',
            name='remita_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
