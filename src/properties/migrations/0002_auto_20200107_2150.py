# Generated by Django 3.0.2 on 2020-01-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
