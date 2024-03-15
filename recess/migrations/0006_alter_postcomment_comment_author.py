# Generated by Django 5.0.2 on 2024-03-01 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recess', '0005_feed_feed_original_importer_feed_feed_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_with_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
