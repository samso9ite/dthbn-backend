# Generated by Django 4.2.6 on 2023-11-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0002_remove_examregistration_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexing',
            name='examination_number1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='examination_number2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='examination_type1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='examination_type2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='examination_year1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='examination_year2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade1_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade2_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade3',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade3_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade4',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade4_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade5',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade5_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade6',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade6_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade7',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grade7_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='o_level_cert1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='o_level_cert2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='qualification1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='qualification2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='qualification3',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_address1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_address2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_name1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_name2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_phone1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='referee_phone2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='school_attended1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='school_attended2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='school_attended3',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub1_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub2_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub3',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub3_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub4',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub4_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub5',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub5_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub6',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub6_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub7',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='sub7_2',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='unapproved',
        ),
        migrations.AddField(
            model_name='indexing',
            name='examinations',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grades',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='o_level_cert',
            field=models.ImageField(blank=True, null=True, upload_to='images/OlevelResult'),
        ),
        migrations.AddField(
            model_name='indexing',
            name='qualifications',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referees',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='school_attended',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
