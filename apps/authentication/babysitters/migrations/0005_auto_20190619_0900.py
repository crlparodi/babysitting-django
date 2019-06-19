# Generated by Django 2.2.2 on 2019-06-19 07:00

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0004_auto_20190614_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='EUR', max_digits=10, verbose_name='Tarifs de vos prestations'),
        ),
    ]