from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    aadhar=models.IntegerField()
    email=models.EmailField()
    mobilenum=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=['name','age','aadhar','email','mobilenum']