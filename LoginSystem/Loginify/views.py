from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import UserDetails

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, world!")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already exists! Try Logging in.")

        UserDetails.objects.create(username=username, email=email, password=password)

        return redirect("login")

    return render(request, "Loginify/signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = UserDetails.objects.filter(email=email).first()

        if not user:
            return HttpResponse("No account found with this email. Please sign up first.")

        if user.password != password:
            return HttpResponse("Incorrect password. Please try again.")

        return HttpResponse("Login Successful!")

    return render(request, 'Loginify/login.html')
