# Generated by Django 3.0.6 on 2020-06-01 15:47

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csts', '0003_auto_20200529_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=50)),
                ('cost_line', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('source_port', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='source_port_set', to='csts.Port')),
                ('target_port', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='target_port_set', to='csts.Port')),
            ],
        ),
    ]