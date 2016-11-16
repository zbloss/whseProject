from django.db import models


class Container(models.Model):
    containerNumber = models.CharField(max_length=20, default="")
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.containerNumber


class Incoming(models.Model):
    name = models.CharField(max_length = 50)
    message = models.TextField()
    containerNumber = models.ForeignKey(Container, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Part(models.Model):
    partNumber = models.CharField(max_length=20)
    quantitySkids = models.IntegerField()
    pcsPerSkid = models.IntegerField()
    containerNumber = models.ForeignKey(Container, on_delete=models.CASCADE)
    def __str__(self):
        return self.partNumber
