from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def HelloAPI(Request):
    return Response({'hello world'})

@api_view(['GET', 'POST'])
def booksAPI(request): #/book/
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        #시리얼라이저에 전체 데이터를 한번에 집어넣기 (직렬화, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK) #Return Response
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        #POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid():
            serializer.save()#create함수를 실행시키는 모델 시리얼라이저의 기능
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request, bid): #/book/<int:id>/
    book = get_object_or_404(Book, bid = bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status = status.HTTP_200_OK)