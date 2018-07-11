# Generated by Django 2.0.6 on 2018-07-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0004_auto_20180710_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babysitter',
            name='Deuxième diplôme (si vous en avez un) ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Moments de la journée ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Premier diplôme (si vous en avez un) ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name="Tranche d'âge de l'enfant ",
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Troisième diplôme (si vous en avez un) ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Votre lieu de résidence ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Votre nom ',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Votre profession ou situation actuelle ',
        ),
        migrations.AddField(
            model_name='babysitter',
            name='2ème diplôme',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='3ème diplôme',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Lieu de naissance',
            field=models.CharField(default=' ', max_length=64),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Moments de la journée',
            field=models.CharField(choices=[('BLANK', ' '), ('AM', 'Matin'), ('PM', 'Après-midi'), ('DAY', 'Toute la journée'), ('EV', 'Toute la soirée')], default='BLANK', max_length=4),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Nom',
            field=models.CharField(default=' ', max_length=42),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Premier diplôme',
            field=models.CharField(choices=[('BLANK', ' '), ('BAF', 'BAFA'), ('DPE', 'Diplôme de petite enfance')], default='BLANK', max_length=4),
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Profession',
            field=models.CharField(choices=[('BLANK', ' '), ('MF', 'Mère au Foyer')], default='BLANK', max_length=4),
        ),
        migrations.AddField(
            model_name='babysitter',
            name="Tranche d'âge de l'enfant",
            field=models.CharField(choices=[('BLANK', ' '), ('BBY', 'Nouveau né (0 à 10 mois)'), ('GBA', 'Nourrisson (10 mois à 2 ans)'), ('CHI', 'Enfants de 2 à 6 ans'), ('GCH', 'Enfants de 7 à 12 ans'), ('TEE', 'Enfants de 12 ans et plus')], default='BLANK', max_length=4),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Âge'),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='price_unit',
            field=models.CharField(choices=[('H', 'Heure'), ('DM', 'Demi-Journée'), ('DAY', 'Jour'), ('WEE', 'Semaine')], default='H', max_length=4, verbose_name='par'),
        ),
    ]