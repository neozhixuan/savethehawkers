# Generated by Django 3.2.3 on 2021-07-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210703_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hawkerstall',
            name='comments',
        ),
        migrations.AddField(
            model_name='hawkerstall',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='project.Comments'),
        ),
    ]
