# Generated by Django 3.2.10 on 2022-01-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsadmin', '0014_alter_doctortimings_pertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropschedule',
            name='day',
            field=models.CharField(blank=True, default=True, max_length=30),
        ),
    ]
