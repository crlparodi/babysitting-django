# Generated by Django 2.0.7 on 2018-07-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0010_auto_20180712_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='age_target',
            field=models.CharField(blank=True, choices=[('BBY', 'Nouveau né (0 à 10 mois)'), ('GBA', 'Nourrisson (10 mois à 2 ans)'), ('CHI', 'Enfants de 2 à 6 ans'), ('GCH', 'Enfants de 7 à 12 ans'), ('TEE', 'Enfants de 12 ans et plus')], max_length=4, verbose_name="Tranche d'âge de l'enfant"),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='grade_main',
            field=models.CharField(blank=True, choices=[('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], max_length=4, verbose_name='Premier diplôme (Si vous en disposez)'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='grade_sec',
            field=models.CharField(blank=True, choices=[('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], max_length=4, verbose_name='2ème diplôme (Si vous en disposez)'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='grade_tri',
            field=models.CharField(blank=True, choices=[('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], max_length=4, verbose_name='3ème diplôme (Si vous en disposez)'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='job',
            field=models.CharField(blank=True, choices=[('MF', 'Mère au Foyer')], max_length=4, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='time_target',
            field=models.CharField(blank=True, choices=[('AM', 'Matin'), ('PM', 'Après-midi'), ('DAY', 'Toute la journée'), ('EV', 'Toute la soirée')], max_length=4, verbose_name='Moments de la journée'),
        ),
    ]
