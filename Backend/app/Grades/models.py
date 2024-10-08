from django.db import models
from app.Students.models import Student
from app.Courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    evaluation_date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"

    