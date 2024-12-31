from django.contrib import auth
from django.shortcuts import render, redirect


def signout_view(request):
    auth.logout(request)
    return redirect("landing:index")


def signup_view(request):
    return render(request, "account/pages/signup.html")


def signin_view(request):
    return render(request, "account/pages/signin.html")
