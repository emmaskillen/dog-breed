# Generated by Django 4.1.5 on 2023-10-28 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='fact',
            new_name='height',
        ),
    ]