# Generated by Django 3.2.19 on 2023-05-19 05:12

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        ('rich_text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='richtext',
            name='cta_text',
            field=models.CharField(blank=True, help_text='text that will be displayed across the button.', max_length=255),
        ),
        migrations.AddField(
            model_name='richtext',
            name='external_url',
            field=models.URLField(blank=True, help_text='Overrides the internal link if set'),
        ),
        migrations.AddField(
            model_name='richtext',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rich_text_richtext_files', to='filer.file', verbose_name='File'),
        ),
        migrations.AddField(
            model_name='richtext',
            name='internal_link',
            field=cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.page'),
        ),
    ]
