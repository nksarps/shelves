from .models import Bookshelf
from .serializers import BookshelfSerializer
from accounts.permissions import IsVerified
from books.models import Book
from books.serializers import BookSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([IsVerified])
def add_bookshelf(request):
    if request.method == 'POST':
        serializer = BookshelfSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            return Response({
                'success':True,
                'bookshelf':serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success':False,
            'message':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsVerified])
def get_all_bookshelves(request):
    if request.method == 'GET':
        bookshelves = Bookshelf.objects.all()

        serializer = BookshelfSerializer(bookshelves, many=True)

        return Response({
            'success':True,
            'bookshelves':serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsVerified])
def get_bookshelf_by_id(request, id:int):
    if request.method == 'GET':
        try:
            shelf = Bookshelf.objects.get(user=request.user, id=id)
        except Bookshelf.DoesNotExist:
            return Response({
                'success':False,
                'message':'Bookshelf does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookshelfSerializer(shelf)

        return Response({
            'success':True,
            'shelf':serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsVerified])
def get_books_in_bookshelf(request, id:int):
    if request.method == 'GET':
        try:
            shelf = Bookshelf.objects.get(user=request.user, id=id)
        except Bookshelf.DoesNotExist:
            return Response({
                'success':False,
                'message':'Bookshelf does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        books = Book.objects.filter(user=request.user, shelf=shelf)

        serializer = BookSerializer(books, many=True)

        return Response({
            'success':True,
            'books':serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsVerified])
def search_bookshelves(request):
    if request.method == 'GET':
        shelves = Bookshelf.objects.filter(user=request.user)

        name = request.query_params.get('name')
        if not name:
            return Response({
                'success':False,
                'message':'Search query is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        results = shelves.filter(name__icontains=name)

        serializer = BookshelfSerializer(results, many=True)

        return Response({
            'success':True,
            'shelves':serializer.data
        })


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_bookshelf(request, id:int):
    if request.method == 'PUT' or request.method == 'PATCH':
        try:
            shelf = Bookshelf.objects.get(user=request.user, id=id)
        except Bookshelf.DoesNotExist:
            return Response({
                'success':False,
                'message':'Bookshelf does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookshelfSerializer(shelf, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({
                'success':True,
                'bookshelf':serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success':False,
            'message':serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_bookshelf(request, id:int):
    if request.method == 'DELETE':
        try:
            shelf = Bookshelf.objects.get(user=request.user, id=id)
        except Bookshelf.DoesNotExist:
            return Response({
                'success':False,
                'message':'Bookshelf does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

        shelf.delete()

        return Response({
            'success':True,
            'message':'Bookshelf deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)