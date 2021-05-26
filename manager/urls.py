
from django.urls import path

from . import views

urlpatterns = [
    path('', views.red_app_home, name="red_app_homepage"),
    path('author/', views.author_home, name="author_homepage"),
    path('author/save', views.save_author, name="save_author"),
    path('author/remove', views.remove_author, name="remove_author"),
    path('book/', views.book_home, name="book_homepage"),
    path('book/save', views.save_book, name="save_book"),
    path('book/remove', views.remove_book, name="remove_book")
]
