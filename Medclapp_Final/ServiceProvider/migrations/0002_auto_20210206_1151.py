# Generated by Django 3.0.7 on 2021-02-06 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecompletion',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]