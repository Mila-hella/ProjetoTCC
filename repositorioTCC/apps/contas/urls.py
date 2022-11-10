from django.urls import path
from .views import UserUpdateView, UserDeleteView, UserCreateView, PasswordView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<pk>", UserUpdateView.as_view(), name="profile"),
    path("delete/<pk>", UserDeleteView.as_view(), name="delete"),
    path("mudar_senha/<pk>", PasswordView.as_view(), name="password")
]