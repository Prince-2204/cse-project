from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Semester(models.Model):
    semester = models.CharField(max_length=100)

    def __str__(self):

        return self.semester

class Years(models.Model):
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.year
    

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.subject


class Course(models.Model):
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.course


class Students(models.Model):
    
    name = models.CharField(max_length=150)
    enrolment_no = models.CharField(max_length=100, primary_key=True)
    exam_roll_no = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year_enrolled = models.ForeignKey(Years,on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.name} {self.enrolment_no}'
    

class student_marks(models.Model):
    student_details = models.ForeignKey(Students,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student_details.name} {self.subject}'

    class Meta:
        unique_together = ['student_details' , 'subject']



class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    student_details = models.ForeignKey(Students,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="Images")
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_details.name} {self.student_details.enrolment_no}'
    
