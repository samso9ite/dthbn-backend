# Generated by Django 4.2.6 on 2023-12-02 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0016_rename_admission_year_indexing_admission_grad_year_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexing',
            old_name='examin_number',
            new_name='exam_number',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='examin_year',
            new_name='exam_year',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='referee_address_2',
            new_name='referee_address',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='referee_name_1',
            new_name='referee_name',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='referee_name_2',
            new_name='referee_name_0',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='referee_phone_1',
            new_name='referee_phone',
        ),
    ]
