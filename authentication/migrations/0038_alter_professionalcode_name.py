# Generated by Django 4.2.6 on 2024-03-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0037_alter_professionalcode_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalcode',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
