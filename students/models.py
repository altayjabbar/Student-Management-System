from django.db import models

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)  # Add max_length
    last_name = models.CharField(max_length=50)  # Add max_length
    email = models.EmailField()
    field_of_study = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
