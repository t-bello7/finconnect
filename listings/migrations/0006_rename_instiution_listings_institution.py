# Generated by Django 3.2.7 on 2021-09-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20210909_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='instiution',
            new_name='institution',
        ),
    ]