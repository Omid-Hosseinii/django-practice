# Generated by Django 4.0.5 on 2022-07-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url_field',
            field=models.URLField(default=None),
        ),
    ]