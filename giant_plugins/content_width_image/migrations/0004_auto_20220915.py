# Generated by Django 2.2 on 2022-06-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_width_image', '0003_auto_20220621_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentwidthimage',
            name='caption',
            field=models.CharField(blank=True, default='', help_text='Add a caption to the image', max_length=255),
        ),
        migrations.AlterField(
            model_name='contentwidthimage',
            name='alt_text',
            field=models.CharField(default='', help_text='Image name', max_length=64),
        ),
    ]
