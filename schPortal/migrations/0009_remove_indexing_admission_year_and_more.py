# Generated by Django 4.2.6 on 2023-11-04 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0008_remove_examregistration_lga_of_origin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexing',
            name='admission_year',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='graduation_year',
        ),
    ]
