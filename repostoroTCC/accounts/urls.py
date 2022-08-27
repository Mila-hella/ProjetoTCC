from django.urls import path
from .views import registerView, UserUpdateView, UserDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", registerView, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<pk>", UserUpdateView.as_view(), name="profile"),
    path("delete/<pk>", UserDeleteView.as_view(), name="delete")
]