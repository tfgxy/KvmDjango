from django.shortcuts import render
from app_test.models import UserPassword
from django.http import HttpResponse


# Create your views here.
def test(request):
    return render(request, 'test.html')


def cal(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a) + int(value_b)
    return render(request, 'result.html', context={'data': result})


def calpage(request):
    return render(request, 'cal.html')


# 建立注册界面的后端
def userpassword(request):
    if request.method == "POST":
        return HttpResponse("successful")
    else:
        return render(request, 'userpassword.html')
    pass


# 后端处理，将post请求发送的数据内容写入到数据表中
def successful(request):
    if request.method == "POST":
        user = request.POST.get('userA')
        password = request.POST.get('passwordA')
        UserPassword.objects.create(user=user, password=password)
        return render(request, 'successful.html')
    else:
        return render(request, 'successful.html')
    pass


def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        readvalue = UserPassword.objects.all()
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    pass


def home(request):
    user = "tfg"
    u = UserPassword.objects.filter(user=user)
    u2=UserPassword.objects.filter(user="erhgareg2424")
    if u2 is None:
        u3="no"
    else:
        u3="yes"
    return render(request, 'home1.html', locals())
