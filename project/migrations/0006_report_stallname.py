# Generated by Django 3.2.3 on 2021-07-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210710_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='stallname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
