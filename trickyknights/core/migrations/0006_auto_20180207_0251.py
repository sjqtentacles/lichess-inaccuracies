# Generated by Django 2.0.1 on 2018-02-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_puzzle_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='game_url',
            field=models.URLField(blank=True),
        ),
    ]