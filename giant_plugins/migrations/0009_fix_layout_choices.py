# Generated by Django 2.2 on 2021-01-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giant_plugins', '0008_add_climatecare_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecardblock',
            name='layout',
            field=models.CharField(choices=[('stacked', 'Stacked'), ('left_right', 'Left/Right')], default='left_right', max_length=255),
        ),
    ]
