from django.db import models

# Create your models here.
class Project(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    periode=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    duty=models.CharField(max_length=500)

class UserPassword(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)