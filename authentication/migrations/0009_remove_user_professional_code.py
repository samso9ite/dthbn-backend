# Generated by Django 3.0.4 on 2020-04-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20200419_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='professional_code',
        ),
    ]