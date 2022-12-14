# Generated by Django 4.0.5 on 2022-07-27 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_chiefeditor_publication_article_publication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'نویسنده', 'verbose_name_plural': 'نویسنده ها'},
        ),
        migrations.AlterModelOptions(
            name='chiefeditor',
            options={'verbose_name': 'سردبیر', 'verbose_name_plural': 'سردبیرها'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'نشریه', 'verbose_name_plural': 'انتشارات'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='T_Article',
        ),
    ]
