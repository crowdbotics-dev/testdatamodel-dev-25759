# Generated by Django 2.2.26 on 2022-07-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_test_dwd"),
    ]

    operations = [
        migrations.CreateModel(
            name="Abc",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("xyz", models.BigIntegerField()),
            ],
        ),
    ]
