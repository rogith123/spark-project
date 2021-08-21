from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

class Account(models.Model):
    ano = models.CharField(max_length=20, primary_key=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.IntegerField()
    atype = models.CharField(max_length=20)

class Transfer(models.Model):
    
    tno =models.AutoField(primary_key=True)
    fromano = models.ForeignKey(Account, related_name='%(class)s_from_account', on_delete=models.CASCADE)
    toano = models.ForeignKey(Account, related_name='%(class)s_to_account', on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    amount = models.IntegerField()