# Generated by Django 3.2.10 on 2021-12-19 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsadmin', '0002_staffcatogory'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffid', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=30)),
                ('joindate', models.DateField()),
                ('experience', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmsadmin.departmentadd')),
                ('staffcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmsadmin.staffcatogory')),
            ],
        ),
    ]
