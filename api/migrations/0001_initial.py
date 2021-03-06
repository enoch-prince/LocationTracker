# Generated by Django 3.2.4 on 2021-06-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_token', models.CharField(max_length=150, verbose_name='Company Token')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=80, verbose_name='Device Serial Number')),
                ('device_model', models.CharField(max_length=50, verbose_name='Device Model')),
                ('app', models.CharField(max_length=50, verbose_name='Registration App Used')),
                ('version', models.CharField(max_length=50, verbose_name='App Version')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated At')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.courier', verbose_name='Courier')),
            ],
        ),
    ]
