# Generated by Django 5.0.6 on 2024-06-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
