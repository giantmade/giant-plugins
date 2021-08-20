# Generated by Django 2.2 on 2021-08-20 02:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('giant_plugins', '0019_urlmixin_file_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentwidthvideo',
            name='youtube_url',
            field=models.URLField(blank=True, help_text="\n            Enter the full URL of the youtube video page. \n            To start the video at a specific time add '?start=xx' to the end of the url (using seconds). \n            You can also add extra paramaters using an ampersand, for example '?start=75&autoplay=1'.\n        ", null=True, validators=[django.core.validators.URLValidator(message='Please enter the full URL of the Youtube video page', regex='www.youtube.com', schemes=['https'])]),
        ),
        migrations.AlterField(
            model_name='featuredcta',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='giant_plugins_featuredcta_files', to='filer.File', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='giant_plugins_heroimage_files', to='filer.File', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='logocard',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='giant_plugins_logocard_files', to='filer.File', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='pagecard',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='giant_plugins_pagecard_files', to='filer.File', verbose_name='File'),
        ),
    ]
