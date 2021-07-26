from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'다시 로그인하세요.'})
    else:
        return render(request, 'login.html')

def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],
                profile_img = request.FILES.get("profile_img"),
                university = request.POST["university"]
            )
            user.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def mypage(request):
    return render(request, 'mypage.html')