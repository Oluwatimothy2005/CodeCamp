# Generated by Django 4.0.6 on 2022-07-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='best_selling',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='latest',
            field=models.BooleanField(),
        ),
    ]