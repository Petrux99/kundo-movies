from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<imdbID>", views.details, name="details"),

    path("api/search/<query>", views.search, name="search")
]
