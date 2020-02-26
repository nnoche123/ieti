from django.db import models


class Strand(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
