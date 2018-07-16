# Generated by Django 2.0.7 on 2018-07-16 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0013_merge_20180716_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('babysitter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='babysittersList.Babysitter')),
                ('is_really_user', models.BooleanField(default=False, verbose_name='Je suis un utilisateur')),
            ],
            bases=('babysittersList.babysitter',),
        ),
    ]
