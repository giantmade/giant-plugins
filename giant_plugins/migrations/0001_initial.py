# Generated by Django 2.1.15 on 2020-07-14 13:41

import cms.models.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import giant_plugins.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentWidthImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_contentwidthimage', serialize=False, to='cms.CMSPlugin')),
                ('alt_text', models.CharField(blank=True, help_text='Image name', max_length=64, null=True)),
                ('caption', models.CharField(blank=True, help_text='Add a caption to the image', max_length=255)),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Content Width Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContentWidthVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_contentwidthvideo', serialize=False, to='cms.CMSPlugin')),
                ('youtube_url', models.URLField(help_text='Enter the full URL of the youtube video page', validators=[django.core.validators.URLValidator(message='Please enter the full URL of the Youtube video page', regex='www.youtube.com', schemes=['https'])])),
                ('title', models.CharField(blank=True, max_length=128)),
                ('alt_title', models.CharField(blank=True, default=models.CharField(blank=True, max_length=128), max_length=128)),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.CreateModel(
            name='PageCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_pagecard', serialize=False, to='cms.CMSPlugin')),
                ('external_url', models.URLField(blank=True, help_text='Overrides the internal link if set')),
                ('title', models.CharField(max_length=256)),
                ('summary', models.CharField(help_text='Limited to 140 characters', max_length=140)),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('internal_link', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.CreateModel(
            name='PageCardBlock',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_pagecardblock', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PullQuote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_pullquote', serialize=False, to='cms.CMSPlugin')),
                ('quote', models.TextField()),
                ('caption', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PullQuoteBlock',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_pullquoteblock', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_richtext', serialize=False, to='cms.CMSPlugin')),
                ('text', giant_plugins.utils.RichTextField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]