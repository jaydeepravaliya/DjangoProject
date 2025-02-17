from django.urls import path
from . import views

urlpatterns = [
    path("hello_world", views.hello_world),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),

    # users CRUD OPERATIONS
    path("users/", views.get_all_users, name="get_all_users"),
    path("users/<str:email>/", views.get_user_by_email, name="get_user_by_email"),
    path("users/<str:email>/update/", views.update_user, name="update_user"),
    path("users/<str:email>/delete/", views.delete_user, name="delete_user"),
]
