# Generated by Django 5.1.7 on 2025-03-25 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='migraines_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField()),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlog.user_login')),
            ],
            options={
                'ordering': ['log_date'],
            },
        ),
    ]
