# Generated by Django 3.0.4 on 2020-06-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0011_examlimit'),
    ]

    operations = [
        migrations.CreateModel(
            name='closeIndexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
