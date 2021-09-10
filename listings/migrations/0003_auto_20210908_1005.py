# Generated by Django 3.2.7 on 2021-09-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210902_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='freqency_type',
            new_name='rate',
        ),
        migrations.AddField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(choices=[('LN', 'Loan'), ('SS', 'Savings'), ('IM', 'Investment'), ('PS', 'Pension'), ('IS', 'Insurance')], default='LN', max_length=2),
        ),
    ]