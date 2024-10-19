# Generated by Django 5.1.2 on 2024-10-18 20:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tags', models.JSONField()),
                ('image_src', models.ImageField(upload_to='images/')),
                ('posted_by', models.CharField(max_length=255)),
                ('time_ago', models.DateTimeField(default=django.utils.timezone.now)),
                ('vote_count', models.IntegerField()),
            ],
        ),
    ]
