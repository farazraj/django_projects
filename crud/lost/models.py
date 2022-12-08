from django.db import models

# Create your models here.

class Crud(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    company = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.name)

class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.loc_name)
