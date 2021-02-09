# Generated by Django 3.0.7 on 2021-02-08 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120, unique=True)),
                ('bloodgroup', models.CharField(choices=[('AB+ve', 'AB+ve'), ('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB-ve', 'AB-ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O-ve', 'O-ve')], max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('dOB', models.DateField(null=True)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('profilepicture', models.ImageField(default=None, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Familymembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('dob', models.DateField()),
                ('relationship', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 2, 8))),
                ('description', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Postfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgrouprequest', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=100)),
                ('patientname', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('location', models.TextField(max_length=250)),
                ('phonenumber', models.CharField(max_length=15)),
                ('date', models.DateField(default=datetime.date(2021, 2, 8))),
                ('time', models.TimeField()),
                ('priority', models.CharField(choices=[('Within 1 Hour', 'Within 1 Hour'), ('Within 6 Hours', 'Within 6 Hours'), ('Within 12 Hours', 'Within 12 Hours'), ('Within 24 Hours', 'Within 24 Hours')], max_length=100)),
            ],
        ),
    ]
