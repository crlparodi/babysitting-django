# Generated by Django 2.0.7 on 2018-07-17 10:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0018_auto_20180716_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=' ', max_length=128),
        ),
    ]
