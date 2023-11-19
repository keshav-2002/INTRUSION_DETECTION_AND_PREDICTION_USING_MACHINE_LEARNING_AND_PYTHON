from email.policy import default
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    Crime = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Income = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    Maritalstatus = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
    Harm = models.CharField(max_length=100)
    Attack = models.CharField(max_length=100)
    AttackMethod = models.CharField(max_length=100)

    def __str__(self):
        return self.Crime,self.Gender,self.Age,self.Income,self.Job,self.Maritalstatus,self.Education,self.Harm,self.Attack,self.AttackMethod

class DoctorFeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)