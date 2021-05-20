# Generated by Django 2.2 on 2021-05-20 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('giant_plugins', '0017_logo_grid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareThisPage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='giant_plugins_sharethispage', serialize=False, to='cms.CMSPlugin')),
                ('linkedin', models.BooleanField(default=False, help_text='Check this to show the LinkedIn share button')),
                ('facebook', models.BooleanField(default=False, help_text='Check this to show the Facebook share button')),
                ('email', models.BooleanField(default=False, help_text='Check this to show the Email share button')),
                ('twitter', models.BooleanField(default=False, help_text='Check this to show the Twitter share button')),
                ('whatsapp', models.BooleanField(default=False, help_text='Check this to show the Whatsapp share button')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
