# Generated by Django 2.2.6 on 2019-10-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_id', models.IntegerField()),
                ('classroom_name', models.TextField()),
                ('assignment_name', models.TextField()),
                ('status', models.TextField()),
                ('time_submitted', models.DateTimeField()),
                ('code', models.TextField()),
                ('student_name', models.TextField()),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
    ]