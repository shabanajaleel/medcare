# Generated by Django 3.2.10 on 2022-01-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsadmin', '0013_doctortimings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortimings',
            name='pertime',
            field=models.CharField(default=True, max_length=30),
        ),
    ]