# Generated by Django 4.2.6 on 2024-03-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0040_rename_name_professionalcode_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank='True', max_length=100, null='True'),
            preserve_default='True',
        ),
    ]
