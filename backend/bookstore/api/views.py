from rest_framework import viewsets
from .models import BookStoreModel
from .serializers import BookStoreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Method1_APIView

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer

# class BookListView(APIView):

#     def get(self, request, format=None):
#         model = BookStoreModel.objects.all()
#         serializer = BookStoreSerializer(model, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookStoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BooklistUpdateDelete(APIView):

#     def get_object(self, pk):
#         try:
#             return BookStoreModel.objects.get(pk=pk)
#         except BookStoreModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookStoreSerializer(book)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookStoreSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Method2_Concrete_APIView

# from rest_framework import viewsets, generics
# from .models import BookStoreModel
# from .serializers import BookStoreSerializer

# # ViewSet for handling all CRUD operations with the router
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer

# # Concrete view for handling list and create operations
# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer

# # Concrete view for handling retrieve, update, and delete operations
# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer


#method3_Shortcut

from rest_framework import viewsets
from .models import BookStoreModel
from .serializers import BookStoreSerializer

# ViewSet for handling all CRUD operations with the router
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer

