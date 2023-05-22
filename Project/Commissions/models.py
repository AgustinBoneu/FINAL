from django.db import models

# Create your models here.
class Commissions_Bank_USF(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    cheques = models.IntegerField(Null=True)
    def __str__(self):
        return self.date
        

class Commissions_Other_Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    cheques = models.IntegerField(Null=True)
    def __str__(self):
        return self.id
    
class Name_Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    name_bank = models.CharField(max_length=50)

# class Increase(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     # date = models.DateField()
#     # cheques = models.IntegerField(Null=True)
