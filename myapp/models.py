from django.db import models


class Name(models.Model):
    user = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.user
