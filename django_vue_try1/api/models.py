from django.db import models

# Create your models here.

class FileNames(models.Model):
  fileName = models.CharField(max_length=1000000)

  def __str__(self):
    return self.fileName
