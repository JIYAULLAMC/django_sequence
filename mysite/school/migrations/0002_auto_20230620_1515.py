# Generated by Django 3.2.19 on 2023-06-20 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stu_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_id',
            new_name='sid',
        ),
    ]
