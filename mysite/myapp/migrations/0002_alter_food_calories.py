# Generated by Django 5.0.6 on 2024-06-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(),
        ),
    ]