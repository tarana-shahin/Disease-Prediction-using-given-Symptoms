# from disease_prediction.views import feedback
from django.db import models

# Create your models 
class Doctor(models.Model):
    Doctor_Id=models.AutoField(primary_key=True)
    DoctorName=models.CharField(max_length=100)
    Disease=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Hospital=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)


    def __str__(self):
        return self.DoctorName


class Feedback(models.Model):
    FeedId=models.AutoField(primary_key=True)
    Did=models.ForeignKey("Doctor",on_delete=models.CASCADE,db_column="Doctor_Id")
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Rating=models.IntegerField()
    Feed=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

