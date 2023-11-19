from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    AGE = models.CharField(max_length=10)
    GENDER = models.CharField(max_length=10)
    CP = models.CharField(max_length=10)
    BP = models.CharField(max_length=10)
    CHOL = models.CharField(max_length=10)
    FBS = models.CharField(max_length=10)
    ECG = models.CharField(max_length=10)
    THALACH = models.CharField(max_length=10)
    EXANG = models.CharField(max_length=10)
    OLD_PEAK = models.CharField(max_length=10)
    SLOPE = models.CharField(max_length=10)
    CA = models.CharField(max_length=10)
    THAL = models.CharField(max_length=10)

    def __str__(self):
        return str(self.AGE)
