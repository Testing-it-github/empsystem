from django.db import models


# Create your models here.

class Employee(models.Model):
    Emp_Name = models.CharField(max_length=100)
    Emp_ID = models.EmailField()
    Designation = models.CharField(max_length=100)
    Date_of_joining = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Annual_CTC = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)

class Latestnews(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title
    

class Calendar(models.Model):
    Date = models.DateField()
    Occasion = models.TextField()

class JobOpening(models.Model):
    role = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    skills = models.TextField()
    current_ctc = models.CharField(max_length=50)
    notice_period = models.CharField(max_length=50)

    def __str__(self):
        return self.role

    

  

