# Generated by Django 3.2.3 on 2021-10-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hawkerstall',
            name='reco',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
