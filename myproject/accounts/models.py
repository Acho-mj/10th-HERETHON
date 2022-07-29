from django.db import models

class People(models.Model):
    person = models.CharField(max_length=8)