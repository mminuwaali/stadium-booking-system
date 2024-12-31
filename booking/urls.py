from . import views
from django.urls import path

app_name, urlpatterns = "booking", [
    path("", views.index_view, name="index"),
    path("<int:id>/", views.detail_view, name="detail"),
]
