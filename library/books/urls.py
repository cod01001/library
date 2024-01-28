from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_index, name="books_index"),
    path("<int:pk>/", views.books_detail, name="books_detail"),
]

