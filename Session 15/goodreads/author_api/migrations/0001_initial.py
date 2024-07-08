# Generated by Django 5.0.6 on 2024-07-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('profile_image', models.URLField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
