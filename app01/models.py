from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)

# class Publisher(models.Model):
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=64,null=False,unique=True)