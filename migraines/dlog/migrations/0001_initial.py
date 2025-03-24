# Generated by Django 5.1 on 2025-03-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='simple_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('log_date', models.DateField()),
            ],
            options={
                'ordering': ['log_date'],
            },
        ),
    ]
