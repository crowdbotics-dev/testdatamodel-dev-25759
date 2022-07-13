from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
    dwd = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Abc(models.Model):
    "Generated Model"
    xyz = models.BigIntegerField()
