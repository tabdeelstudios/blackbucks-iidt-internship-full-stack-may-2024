# Generated by Django 5.0.6 on 2024-06-26 12:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('status', models.BooleanField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'notes',
                'ordering': ['-createdAt'],
            },
        ),
    ]
