# Generated by Django 2.0.1 on 2018-02-05 23:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180203_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]