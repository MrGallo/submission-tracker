# Generated by Django 2.1 on 2018-09-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.TextField(max_length=15),
        ),
    ]