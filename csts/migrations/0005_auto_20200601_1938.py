# Generated by Django 3.0.6 on 2020-06-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csts', '0004_transportedge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transportedge',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
