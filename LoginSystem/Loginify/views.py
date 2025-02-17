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
        email = request.POST["email"]
        password = request.POST["password"]

        user = UserDetails.objects.filter(email=email).first()

        if not user:
            return HttpResponse(
                "No account found with this email. Please sign up first."
            )

        if user.password != password:
            return HttpResponse("Incorrect password. Please try again.")

        return HttpResponse("Login Successful!")

    return render(request, "Loginify/login.html")


# Get all users
def get_all_users(request):
    users = UserDetails.objects.all()
    user_list = "<br>".join([f"{user.username} - {user.email}" for user in users])
    return HttpResponse(f"All Users:<br>{user_list}")


# Get a single user by email
def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return HttpResponse(f"User Found: {user.username} - {user.email}")
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found.")


# Update user details
def update_user(request, email):
    if request.method == "POST":
        try:
            user = UserDetails.objects.get(email=email)
            user.username = request.POST.get("username", user.username)
            user.password = request.POST.get("password", user.password)
            user.save()
            return HttpResponse(f"User {email} updated successfully.")
        except UserDetails.DoesNotExist:
            return HttpResponse("User not found.")
    return HttpResponse("Invalid request method. Use POST.")


# Delete user by email
def delete_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user.delete()
        return HttpResponse(f"User {email} deleted successfully.")
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found.")
