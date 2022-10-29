# Generated by Django 4.1.1 on 2022-10-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_actors',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movies.actor'),
        ),
        migrations.AddField(
            model_name='serial',
            name='serial_actors',
            field=models.ManyToManyField(blank=True, related_name='series', to='movies.actor'),
        ),
    ]