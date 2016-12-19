from django.db import models

class Part(models.Model):
    partNumber = models.CharField(max_length=20)
    pcsPerSkid = models.IntegerField()
    def __str__(self):
        return self.partNumber



class Container(models.Model):
    containerNumber = models.CharField(default="", max_length=30)
    date = models.DateField()
    time = models.TimeField()
    part1 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty1 = models.IntegerField(default=0)
    part2 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty2 = models.IntegerField(default=0)
    part3 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty3 = models.IntegerField(default=0)
    part4 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty4 = models.IntegerField(default=0)
    part5 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty5 = models.IntegerField(default=0)
    part6 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty6 = models.IntegerField(default=0)
    part7 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty7 = models.IntegerField(default=0)
    part8 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty8 = models.IntegerField(default=0)
    part9 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty9 = models.IntegerField(default=0)
    part10 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty10 = models.IntegerField(default=0)
    part11 = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty11 = models.IntegerField(default=0)

    def __str__(self):
        return self.containerNumber


