from .models import Book
from .serializers import BookSerializer
from accounts.models import User
from accounts.permissions import IsVerified
from bookshelves.models import Bookshelf
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([IsVerified])
def add_book(request, shelf_id:int):
    if request.method == 'POST':
        try:
            shelf = Bookshelf.objects.get(user=request.user, id=shelf_id)
        except Bookshelf.DoesNotExist:
            return Response({
                'success':True,
                'message':'Bookshelf does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(data=request.data)
        print(request.user)

        if serializer.is_valid():
            serializer.save(user=request.user, shelf=shelf)

            return Response({
                'success':True,
                'book':serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success':False,
            'message':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsVerified])
def get_book_by_id(request, id:str):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=id, user=request.user)
        except Book.DoesNotExist:
            return Response({
                'success':False,
                'message':'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)

        return Response({
            'success':True,
            'book':serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsVerified])
def get_book_by_isbn(request, isbn:str):
    if request.method == 'GET':
        try:
            book = Book.objects.get(isbn=isbn, user=request.user)
        except Book.DoesNotExist:
            return Response({
                'success':False,
                'message':'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)

        return Response({
            'success':True,
            'book':serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsVerified])
def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.filter(user=request.user)

        serializer = BookSerializer(books, many=True)

        return Response({
            'success':True,
            'books':serializer.data
        })

@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_book(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        try:
            book = Book.objects.get(id=id, user=request.user)
        except Book.DoesNotExist:
            return Response({
                'success':False,
                'message':'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'success':True,
                'message':'Book updated successfully',
                'book':serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success':False,
            'message':serializer.errors
        }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_book(request, id:str):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(id=id, user=request.user)
        except Book.DoesNotExist:
            return Response({
                'success':False,
                'message':'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()

        return Response({
            'success':True,
            'message':'Book deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsVerified])
def search_books(request):
    if request.method == 'GET':
        query = request.query_params.get('query')
        books = Book.objects.filter(user=request.user)

        if not query:
            return Response({
                'success':False,
                'message':'Search query required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        results = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

        serializer = BookSerializer(results, many=True)

        return Response({
            'success':True,
            'message':'Below are the search results:',
            'books':serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsVerified])
def filter_books_by_genre(request):
    if request.method == 'GET':
        books = Book.objects.filter(user=request.user)

        genre = request.query_params.get('genre')
        if not genre:
            return Response({
                'success':False,
                'message':'Genre is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        results = books.filter(genre__iexact=genre)

        serializer = BookSerializer(results, many=True)

        return Response({
            'success':True,
            'books':serializer.data
        }, status=status.HTTP_200_OK)