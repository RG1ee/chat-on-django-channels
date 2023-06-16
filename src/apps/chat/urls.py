from django.urls import path

from src.apps.chat import views


urlpatterns = [
    path("", views.index, name="index"),
]
