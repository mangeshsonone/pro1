from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mobno=models.CharField(max_length=100)
