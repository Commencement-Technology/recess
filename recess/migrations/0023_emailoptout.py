# Generated by Django 5.0.2 on 2024-03-29 02:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recess', '0022_alter_lock_lock_expiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailOptOut',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('opt_out_token', models.UUIDField(default=uuid.uuid4)),
                ('opted_out', models.BooleanField(default=False)),
            ],
        ),
    ]
