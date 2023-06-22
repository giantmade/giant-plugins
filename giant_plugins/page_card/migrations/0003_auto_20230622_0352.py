# Generated by Django 3.2.19 on 2023-06-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_card', '0002_auto_20220701_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecard',
            name='new_tab',
            field=models.BooleanField(default=False, help_text='Open this link in a new tab/window.'),
        ),
        migrations.AddField(
            model_name='pagecardblock',
            name='anchor_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
