# Generated by Django 5.0.2 on 2024-02-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recess', '0002_feed_feed_picture_url_alter_user_feeds_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feed_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feed',
            name='feed_url',
            field=models.URLField(unique=True),
        ),
    ]
