# Generated by Django 3.2.19 on 2023-06-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroimage',
            name='new_tab',
            field=models.BooleanField(default=False, help_text='Open this link in a new tab/window.'),
        ),
    ]
