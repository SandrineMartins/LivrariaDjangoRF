from email.mime import image
from .serializers import BooksSerializer
from .models import Books
from rest_framework.response import Response
from rest_framework.decorators import api_view

    
@api_view(['GET'])
def BooksList(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BookDetail(request, pk):
    books = Books.objects.get(id_book=pk)
    serializer = BooksSerializer(books, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def BookCreate(request):    
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid():        
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def BookUpdate(request, pk):
    books = Books.objects.get(id_book=pk)
    serializer = BooksSerializer(instance=books, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def BookDelete(request, pk):
    books = Books.objects.get(id_book=pk)    
    books.delete()

    return Response('Deleted')
    