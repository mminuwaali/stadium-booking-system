from . import views
from django.urls import path

app_name, urlpatterns = "account", [
    path("signup/", views.signup_view, name="signup"),
    path("signin/", views.signin_view, name="signin"),
    path("signout/", views.signout_view, name="signout"),
]
