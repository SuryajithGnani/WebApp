# Generated by Django 3.2.5 on 2021-07-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_movie_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='ratings',
            field=models.CharField(max_length=250),
        ),
    ]
