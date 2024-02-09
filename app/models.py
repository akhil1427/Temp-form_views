from django.db import models

# Create your models here.

class collage(models.Model):
    clg_name=models.CharField(max_length=100)
    clg_princ=models.CharField(max_length=100)

    def __str__(self):
        return self.clg_name
