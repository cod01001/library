from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_index, name="books_index"),
    path("book/<int:pk>/", views.books_detail, name="books_detail"),
    path("category/<str:category>/", views.books_category, name="books_category"),
    path("author/<str:author>/", views.books_name_author, name="books_author"),
]
