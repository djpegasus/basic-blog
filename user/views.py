from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from article.models import Article


# Create your views here.
def registerUser(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect("index")
    return render(request, "register.html", {"form":form})

def loginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "Kullanıcı Adı veya Şifre Hatalıdır.")
            return render(request,"login.html", {"form":form})
        login(request, user)
        messages.success(request, "Girişiniz Başarı ile Yapılmıştır.")
        return redirect("index")
    return render(request,"login.html", {"form":form})

def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış Başarı ile Yapılmıştır.")
    return redirect("index")

@login_required(login_url="users:login")
def dashboard(request):
    article = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"article":article})
