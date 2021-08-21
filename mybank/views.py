from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    acc = Account.objects.all()
    txn = Transfer.objects.all()
    return render(request,'index.html',{'acc':acc,'txn':txn})

def account(request,ano):
    acc = Account.objects.get(pk=ano)
    toacc = Account.objects.all()
    return render(request,'transfer.html',{'acc':acc,'toacc':toacc})

def transfermoney(request):
    if request.method == 'POST':
        fromano = request.POST['fromano']
        toano = request.POST['toano']
        date = request.POST['date']
        amount = request.POST['amount']
        f = Account.objects.get(ano=fromano)
        t = Account.objects.get(ano=toano)
        if f.ano != t.ano:
            if int(f.balance) > int(amount):
                ttot = int(t.balance) + int(amount)
                ftot = int(f.balance) - int(amount)
                Account.objects.filter(ano=toano).update(balance=ttot)
                Account.objects.filter(ano=fromano).update(balance=ftot)
                Transfer.objects.create(fromano=f,toano=t,date=date,amount=amount)
                return render(request,'msg.html',{'msg':'Transaction Successfull'})
            else:
                return render(request,'msg.html',{'msg':'Insufficient Balance'})
        else:
            return render(request,'msg.html',{'msg':'Both accounts cannot be same'})

def about(request):
    return render(request,'about.html')