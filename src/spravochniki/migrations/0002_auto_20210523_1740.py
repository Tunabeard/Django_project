# Generated by Django 3.2.3 on 2021-05-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Издатель', 'verbose_name_plural': 'Издатели'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Серия', 'verbose_name_plural': 'Серии'},
        ),
    ]
