# Generated by Django 4.0.6 on 2022-07-22 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo')),
                ('carousel1', models.ImageField(upload_to='carousel')),
                ('carousel2', models.ImageField(upload_to='carousel')),
                ('carousel3', models.ImageField(upload_to='carousel')),
                ('banner', models.ImageField(upload_to='banner')),
                ('favicon', models.ImageField(upload_to='favicon')),
                ('about', models.TextField()),
                ('copyright', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(default='a', unique=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Type',
                'db_table': 'Type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('pix', models.ImageField(upload_to='pix')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('network', models.CharField(max_length=50)),
                ('launch', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('camera', models.CharField(max_length=50)),
                ('feature', models.BooleanField()),
                ('best_selling', models.BooleanField(default=True)),
                ('latest', models.BooleanField(default=True)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.type')),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phone',
                'db_table': 'phone',
                'managed': True,
            },
        ),
    ]
