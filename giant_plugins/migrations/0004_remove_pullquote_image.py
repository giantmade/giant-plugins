# Generated by Django 2.2 on 2020-09-14 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giant_plugins', '0003_pullquote_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pullquote',
            name='image',
        ),
    ]