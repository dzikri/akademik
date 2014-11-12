from django.db import models

class Biodata(models.Model):
    nama = models.Charfield(max_length=100)
    

# Create your models here.
