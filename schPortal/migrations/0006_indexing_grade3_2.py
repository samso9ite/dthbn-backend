# Generated by Django 3.0.4 on 2021-03-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0005_indexing_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexing',
            name='grade3_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
