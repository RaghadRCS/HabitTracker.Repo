from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

