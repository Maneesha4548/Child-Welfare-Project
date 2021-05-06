# Generated by Django 3.0 on 2021-04-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210430_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Donor'), (2, 'Organisation'), (3, 'Guest')], default=3),
        ),
    ]