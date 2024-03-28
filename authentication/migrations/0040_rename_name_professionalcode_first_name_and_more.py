# Generated by Django 4.2.6 on 2024-03-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0039_delete_professional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionalcode',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='professionalcode',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professionalcode',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
