from django.db import models


# Create your models here.
class UserAnalysis(models.Model):
    img = models.ImageField(name='img', upload_to='media')
