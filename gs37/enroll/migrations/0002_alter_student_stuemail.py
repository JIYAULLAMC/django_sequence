# Generated by Django 4.1.6 on 2023-05-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enroll", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="stuemail",
            field=models.EmailField(max_length=50),
        ),
    ]
