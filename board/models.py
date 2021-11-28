from django.db import models
from django.db.models.base import Model

# Create your models here.
class justCount(models.Model):
    좋아요 = models.IntegerField()