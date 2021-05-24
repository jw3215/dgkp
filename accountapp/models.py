from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
