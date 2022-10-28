from django.db import models

# Create your models here.
from django.db import models

class Profile(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.slackUsername 