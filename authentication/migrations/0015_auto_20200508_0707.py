# Generated by Django 3.0.4 on 2020-05-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_user_school_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school_logo',
            field=models.FileField(null=True, upload_to='images/school/sch_logo'),
        ),
    ]
