# Generated by Django 2.0.7 on 2018-07-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0006_auto_20180712_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babysitter',
            name='2ème diplôme',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='3ème diplôme',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Lieu de naissance',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Moments de la journée',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Premier diplôme',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Profession',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name="Tranche d'âge de l'enfant",
        ),
        migrations.AddField(
            model_name='babysitter',
            name='age_target',
            field=models.CharField(choices=[('BLANK', ' '), ('BBY', 'Nouveau né (0 à 10 mois)'), ('GBA', 'Nourrisson (10 mois à 2 ans)'), ('CHI', 'Enfants de 2 à 6 ans'), ('GCH', 'Enfants de 7 à 12 ans'), ('TEE', 'Enfants de 12 ans et plus')], default='BLANK', max_length=4, verbose_name="Tranche d'âge de l'enfant"),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='birth_location',
            field=models.CharField(default=' ', max_length=64, verbose_name='Lieu de naissance'),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='grade_main',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4, verbose_name='Premier diplôme (Si vous en disposez)'),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='grade_sec',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4, verbose_name='2ème diplôme (Si vous en disposez)'),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='grade_tri',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4, verbose_name='3ème diplôme (Si vous en disposez)'),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='job',
            field=models.CharField(choices=[('BLANK', ' '), ('MF', 'Mère au Foyer')], default='BLANK', max_length=4, verbose_name='Profession'),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='time_target',
            field=models.CharField(choices=[('BLANK', ' '), ('AM', 'Matin'), ('PM', 'Après-midi'), ('DAY', 'Toute la journée'), ('EV', 'Toute la soirée')], default='BLANK', max_length=4, verbose_name='Moments de la journée'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='nurse_name',
            field=models.CharField(default=' ', max_length=42, verbose_name='Nom'),
        ),
    ]
