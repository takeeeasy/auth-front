from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=20)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.id
