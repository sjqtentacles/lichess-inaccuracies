# Generated by Django 2.0.1 on 2018-02-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_game_game_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='pgn',
            field=models.TextField(max_length=5000),
        ),
    ]
