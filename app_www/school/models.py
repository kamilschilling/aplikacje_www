from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.surname


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    value = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.subject
