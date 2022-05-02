# Generated by Django 4.0.4 on 2022-05-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackage',
            name='available_places',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Maximum Capacity of travelers', null=True),
        ),
    ]