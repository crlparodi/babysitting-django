# Generated by Django 2.1 on 2018-08-21 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='accounts',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='babysitter_profile', to=settings.AUTH_USER_MODEL, verbose_name='Membre'),
        ),
    ]
