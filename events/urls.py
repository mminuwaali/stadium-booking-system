from . import views
from django.urls import path

app_name, urlpatterns = "events", [
    path("", views.index_view, name="index"),
    path("<int:id>/", views.detail_view, name="detail"),
]
