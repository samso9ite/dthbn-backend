# Generated by Django 4.2.6 on 2023-11-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schPortal', '0012_alter_indexing_grades'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexing',
            old_name='referees',
            new_name='admission_year',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='examinations',
            new_name='examination_number1',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='school_attended',
            new_name='graduation_year',
        ),
        migrations.RenameField(
            model_name='indexing',
            old_name='o_level_cert',
            new_name='o_level_cert1',
        ),
        migrations.RemoveField(
            model_name='indexing',
            name='grades',
        ),
        migrations.AddField(
            model_name='indexing',
            name='examination_number2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='examination_type1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='examination_type2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='examination_year1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='examination_year2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade1_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade2_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade3_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade4_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade5_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade6',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade6_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade7',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='grade7_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='o_level_cert2',
            field=models.ImageField(blank=True, null=True, upload_to='images/OlevelResult'),
        ),
        migrations.AddField(
            model_name='indexing',
            name='qualification1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='qualification2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='qualification3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_address1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_address2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_name1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_name2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_phone1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='referee_phone2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='school_attended1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='school_attended2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='school_attended3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub1_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub2_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub3_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub4_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub5_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub6',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub6_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub7',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='sub7_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='indexing',
            name='unapproved',
            field=models.BooleanField(default=False),
        ),
    ]
