# Generated by Django 4.2.6 on 2024-03-16 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/professional/prof_profile_img')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('postal_address', models.CharField(blank=True, max_length=200, null=True)),
                ('religion', models.CharField(blank=True, max_length=200, null=True)),
                ('residential_country', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_state', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_lga', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=200, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=200, null=True)),
                ('maiden_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lga_state', models.CharField(blank=True, max_length=100, null=True)),
                ('senatorial_district', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=30, null=True)),
                ('state_of_birth', models.CharField(blank=True, max_length=100, null=True)),
                ('lga_of_birth', models.CharField(blank=True, max_length=100, null=True)),
                ('qualification1', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification2', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification3', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification4', models.CharField(blank=True, max_length=200, null=True)),
                ('prof_qualification1', models.CharField(blank=True, max_length=200, null=True)),
                ('prof_qualification2', models.CharField(blank=True, max_length=200, null=True)),
                ('prof_qualification3', models.CharField(blank=True, max_length=200, null=True)),
                ('prof_qualification4', models.CharField(blank=True, max_length=200, null=True)),
                ('employment_status', models.CharField(blank=True, max_length=50, null=True)),
                ('present_position', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('office_name', models.CharField(blank=True, max_length=100, null=True)),
                ('office_address', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('office_country', models.CharField(blank=True, max_length=100, null=True)),
                ('office_state', models.CharField(blank=True, max_length=100, null=True)),
                ('office_lga', models.CharField(blank=True, max_length=100, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('office_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('updated', models.BooleanField(default=False)),
                ('state_of_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('lga_of_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('n', models.CharField(max_length=100)),
                ('profuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]