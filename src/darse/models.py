from django.db import models
from django.db.models import Model

# Create your models here.

import datetime

class Post(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    summary     = models.TextField(default="Wow this is Cool!")
    # datetime    = datetime.now()
    # timezone    = django.utils.timezone.now()
   

