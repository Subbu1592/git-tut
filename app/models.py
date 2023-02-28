from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    school = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name