from django.db import models

class insertDatabase(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    topic=models.TextField()
    describe=models.TextField()
    field=models.FileField(upload_to='insert_img/',max_length=250,null=True,default=None)

class newsTable(models.Model):
    name=models.CharField(max_length=50)
    topic=models.TextField()
    describe=models.TextField()
    field=models.FileField(upload_to='news/',max_length=250,null=True,default=None)

class image_gallary(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image_gallaye/',null=True,blank=None)