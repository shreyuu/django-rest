from django.db import models

class Student(models.Model):
    objects=models.Manager()
    stud_name = models.CharField(max_length=255)
    stud_id = models.IntegerField()
    
    def __str__(self):
        return f'Student ({self.stud_name},{self.stud_id})'
    
class Department(models.Model):
    objects =  models.Manager()
    dept_name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.dept_name