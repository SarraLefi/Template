from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()
    def __str__(self):
        return self.username