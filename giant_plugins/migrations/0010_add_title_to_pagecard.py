# Generated by Django 2.2 on 2021-01-14 09:34

from django.db import migrations
import giant_plugins.utils


class Migration(migrations.Migration):

    dependencies = [
        ('giant_plugins', '0009_fix_layout_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecardblock',
            name='title',
            field=giant_plugins.utils.RichTextField(blank=True),
        ),
    ]
