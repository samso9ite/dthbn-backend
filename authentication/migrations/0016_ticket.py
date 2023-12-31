# Generated by Django 3.0.4 on 2020-05-14 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_auto_20200508_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ticket_status', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=20)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='images/ticket_attachments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
