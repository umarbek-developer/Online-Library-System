from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import book_seralizers
from apps.book.models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BookListApiView(ListAPIView):
    serializer_class = book_seralizers.BookListSeralzier
    queryset = Book.objects.filter(is_deleted=False)
    

class BookCreateApiView(CreateAPIView):
    serializer_class = book_seralizers.BookCreateSeralzier
    queryset = Book.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        data['published_user'] = request.user.id
        ser = self.serializer_class(data=request.data)
        ser.user = request.user
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response({
            "message": "successfully craeted",
            "data": ser.data
        })


class BookUpdateApiView(UpdateAPIView):
    serializer_class = book_seralizers.BookUpdateSeralzier
    queryset = Book.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            wishlist = self.queryset.get(id=pk, published_user=request.user)
            ser = self.serializer_class(wishlist, data=request.data, partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
            return Response({
                "message": "wishlist updated successfully",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({
                "message": "wishlist not found",
            }, status=status.HTTP_404_NOT_FOUND)
            


class BookDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Book.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            book = self.queryset.get(id=pk, published_user=request.user)
            book.is_deleted = True
            book.save()
            return Response({
                "message": "book deleted",
            }, status=status.HTTP_202_ACCEPTED)
        except Book.DoesNotExist:
            return Response({
                "message": "book not found",
            }, status=status.HTTP_404_NOT_FOUND)
        

