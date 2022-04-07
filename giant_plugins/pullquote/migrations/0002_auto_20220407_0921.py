# Generated by Django 2.2 on 2022-04-07 09:21

from django.db import migrations, models
import giant_plugins.utils


class Migration(migrations.Migration):

    dependencies = [
        ('pullquote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullquote',
            name='text_side',
            field=models.CharField(choices=[('right', 'Right'), ('left', 'Left')], default='right', max_length=255),
        ),
        migrations.AlterField(
            model_name='pullquote',
            name='quote',
            field=giant_plugins.utils.RichTextField(),
        ),
    ]