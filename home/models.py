from django.db import models

class Incoming(models.Model):
    name = models.CharField(max_length = 50)
    message = models.TextField()
    def __str__(self):
        return self.title
