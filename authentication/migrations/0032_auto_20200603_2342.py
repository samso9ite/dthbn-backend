# Generated by Django 3.0.4 on 2020-06-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0031_user_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.AddField(
            model_name='user',
            name='is_exam_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_indexing_staff',
            field=models.BooleanField(default=False),
        ),
    ]
