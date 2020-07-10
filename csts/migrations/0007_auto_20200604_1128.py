# Generated by Django 3.0.6 on 2020-06-04 11:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csts', '0006_transportedge_travel_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='cost_down',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5, verbose_name='Цена разгрузки 1м3'),
        ),
        migrations.AlterField(
            model_name='port',
            name='cost_up',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5, verbose_name='Цена погрузки 1м3'),
        ),
        migrations.AlterField(
            model_name='port',
            name='country_name',
            field=models.CharField(max_length=50, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='port',
            name='port_name',
            field=models.CharField(max_length=50, verbose_name='Порт'),
        ),
    ]