# Generated by Django 2.2.26 on 2022-07-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='dwd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
