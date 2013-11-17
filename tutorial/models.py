from django.db import models

# tutorial/models.py
class Person(models.Model):
    name = models.CharField(verbose_name="full name")
