from django.db import models


class Container(models.Model):
    containerNumber = models.CharField(max_length=20, default="")
    date = models.DateField()
    time = models.TimeField()
    part1 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty1 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part2 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty2 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part3 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    part4 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty4 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part5 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty5 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part6 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty6 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part7 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty7 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part8 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty8 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part9 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty9 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part10 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty10 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)
    part11 = models.CharField(default="", blank=True, null=True, max_length=15)
    qty11 = models.PositiveSmallIntegerField(default='0', blank=True, null=True)


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
