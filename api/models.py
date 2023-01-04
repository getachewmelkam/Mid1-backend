from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10)
    grade=models.CharField(max_length=2)
    def __str__(self):
        return self.name
