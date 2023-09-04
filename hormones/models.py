from django.db import models


class Hormone(models.Model):
    hormone_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.hormone_name}'


class Record(models.Model):
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.record_date}'


class RecordValue(models.Model):
    hormone = models.ForeignKey(to=Hormone, on_delete=models.CASCADE)
    record = models.ForeignKey(to=Record, on_delete=models.CASCADE, null=True)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.hormone} : {self.record}'
