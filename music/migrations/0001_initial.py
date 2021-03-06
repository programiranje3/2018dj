# Generated by Django 2.1.4 on 2018-12-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_band', models.BooleanField(choices=[[True, 'band'], [False, 'musician']], default=False, verbose_name='Band/Musician')),
            ],
        ),
    ]
