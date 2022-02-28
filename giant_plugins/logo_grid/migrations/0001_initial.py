# Generated by Django 2.2 on 2022-02-28 04:44

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('filer', '0014_folder_permission_choices'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoBlock',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='logo_grid_logoblock', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LogoCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='logo_grid_logocard', serialize=False, to='cms.CMSPlugin')),
                ('external_url', models.URLField(blank=True, help_text='Overrides the internal link if set')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_grid_logocard_files', to='filer.File', verbose_name='File')),
                ('internal_link', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.Page')),
                ('logo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='company_logo', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]