from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    qualification = models.CharField(max_length=40)
    status = models.CharField(max_length=40,default="", editable=True)

    def __str__(self):
        return self.mail



class upload(models.Model):
    filename = models.CharField(max_length=100)
    #description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename


