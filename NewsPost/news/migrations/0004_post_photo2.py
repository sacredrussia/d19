# Generated by Django 4.2.11 on 2024-03-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos2/%Y/%m/%d/', verbose_name='Фото 2'),
        ),
    ]