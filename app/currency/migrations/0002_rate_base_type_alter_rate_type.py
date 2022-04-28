# Generated by Django 4.0.2 on 2022-04-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='base_type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], default='UAH', max_length=5),
        ),
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], max_length=5),
        ),
    ]