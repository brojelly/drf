from django.urls import path
from .fbv_views import HelloAPI, bookAPI, booksAPI
from .cbv_views import BooksAPI, BookAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),

]