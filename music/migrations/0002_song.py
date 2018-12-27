# Generated by Django 2.1.3 on 2018-12-25 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.TimeField(blank=True, default=datetime.time(0, 3), null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('performer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Performer')),
            ],
        ),
    ]