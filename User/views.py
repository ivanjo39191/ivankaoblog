from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request,"login.html",context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from',reverse('home')))

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            #創建用戶
            user = User() #創建物件
            user.username = username
            user.email = email
            user.set_password(password) #儲存密文密碼
            user.save() #將用戶資料儲存至資料庫
            #登錄用戶
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('home')))
    else:
        register_form = RegisterForm()
    context = {}
    context['register_form'] = register_form
    return render(request, "register.html", context)