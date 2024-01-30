from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.books_detail, name="books_detail"),
    path("<category>/", views.books_category, name="books_category"),
    path("", views.books_index, name="books_index"),
]

