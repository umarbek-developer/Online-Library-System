from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import borrow_seralizer
from apps.book.models import Borrow
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class BorrowListApiView(ListAPIView):
    serializer_class = borrow_seralizer.BorrowListSeralzier
    queryset = Borrow.objects.filter(is_deleted=False)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

class BorrowCreateApiView(CreateAPIView):
    serializer_class = borrow_seralizer.BorrowCreateSeralzier
    queryset = Borrow.objects.filter(is_deleted=False)

    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        data['user'] = request.user.id
        ser = self.serializer_class(data=request.data)
        ser.user = request.user
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response({
            "message": "successfully added",
            "data": ser.data
        })




class BorrowUpdateApiView(UpdateAPIView):
    serializer_class = borrow_seralizer.BorrowUpdateSeralzier
    queryset = Borrow.objects.filter(is_deleted=False)

    permission_classes = [IsAuthenticated]

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            borrowed = self.queryset.get(id=pk, user=request.user)
            ser = self.serializer_class(borrowed, data=request.data, partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
            return Response({
                "message": "borrowed updated successfully",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        except Borrow.DoesNotExist:
            return Response({
                "message": "borrowed not found",
            }, status=status.HTTP_404_NOT_FOUND)
            



class BorrowDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Borrow.objects.filter(is_deleted=False)

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            borrowed = self.queryset.get(id=pk, user=request.user)
            borrowed.is_deleted = True
            borrowed.save()
            return Response({
                "message": "borrowed deleted",
            }, status=status.HTTP_202_ACCEPTED)
        except Borrow.DoesNotExist:
            return Response({
                "message": "borrowed not found",
            }, status=status.HTTP_404_NOT_FOUND)
        

