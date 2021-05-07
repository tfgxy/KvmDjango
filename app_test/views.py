from django.shortcuts import render
from app_test.models import UserPassword
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request,'test.html')

def cal(request):
    value_a=request.POST['valueA']
    value_b=request.POST['valueB']
    result=int(value_a)+int(value_b)
    return render(request,'result.html',context={'data':result})

def calpage(request):
    return render(request, 'cal.html')

def userpassword1(request):
    user=request.POST['user']
    password=request.POST['password']
    UserPassword.objects.create(user=user,password=password)
    return render(request, 'userpassword.html')