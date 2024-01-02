from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class data(models.Model):
    npm = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)

    
# Create your models here.
