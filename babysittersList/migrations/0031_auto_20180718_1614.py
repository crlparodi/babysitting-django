# Generated by Django 2.0.7 on 2018-07-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0030_auto_20180718_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='price_unit',
            field=models.CharField(choices=[('TU1', 'Heure'), ('TU2', 'Demi-Journée'), ('TU3', 'Jour'), ('TU4', 'Semaine')], default='H', max_length=4, verbose_name='par'),
        ),
    ]
