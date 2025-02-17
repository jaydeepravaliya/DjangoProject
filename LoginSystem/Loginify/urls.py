from django.urls import path, include
from . import views

urlpatterns = [
    path("hello_world", views.hello_world),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
