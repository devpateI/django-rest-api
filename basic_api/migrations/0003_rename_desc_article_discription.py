# Generated by Django 3.2.9 on 2021-11-25 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_api', '0002_article_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='desc',
            new_name='discription',
        ),
    ]
