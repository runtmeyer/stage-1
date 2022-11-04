from django.db import models

# Create your models here.
from django.db import models

#class Profile(models.Model):
    #slackUsername = models.CharField(max_length=100)
    #backend = models.BooleanField()
    #age = models.IntegerField()
    #bio = models.TextField(max_length=300)

    #def __str__(self):
       # return self.slackUsername 

class Input(models.Model):

    OPERATION_CHOICES = [
        ("addition", "add"),
        ("multiplication", "multiply"),
        ("subtraction", "minus"),
    ]
    operation_type = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    x = models.IntegerField()
    y = models.IntegerField() 