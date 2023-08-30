from django.db import models


class Hormone(models.Model):
    hormone_name = models.CharField(max_length=50)
    description = models.TextField()


class Record(models.Model):
    record_date = models.DateTimeField()
    hormone = models.ForeignKey(to=Hormone, on_delete=models.CASCADE)