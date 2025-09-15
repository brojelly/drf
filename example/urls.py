from django.urls import path
from .fbv_views import HelloAPI, bookAPI, booksAPI
from .cbv_views import BooksAPI, BookAPI
from .mixins_view import BooksAPIMixins, BookAPIMixins

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path("mixin/books", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>", BookAPIMixins.as_view()),
]