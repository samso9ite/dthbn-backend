# Generated by Django 4.2.6 on 2024-01-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0019_indexing_lga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexing',
            old_name='o_level_cert_1',
            new_name='o_level_cert',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='o_level_cert_2',
            new_name='o_level_cert_0',
        ),
    ]
