from . import views
from django.urls import path

app_name, urlpatterns = "landing", [
    path("", views.index_view, name="index"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]
