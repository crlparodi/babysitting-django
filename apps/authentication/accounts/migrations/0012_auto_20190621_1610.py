# Generated by Django 2.2.2 on 2019-06-21 14:10

import apps.authentication.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190619_0850'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='accounts',
            managers=[
                ('objects', apps.authentication.accounts.models.MemberManager()),
            ],
        ),
    ]
