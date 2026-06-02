from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.user.serializers import wishlist_seralizer
from apps.book.models import Wishlist
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class WishlistListApiView(ListAPIView):
    serializer_class = wishlist_seralizer.WishlistListSeralzier
    queryset = Wishlist.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

class WishlistCreateApiView(CreateAPIView):
    serializer_class = wishlist_seralizer.WishlistCreateSeralzier
    queryset = Wishlist.objects.all()
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




class WishlistDeleteApiView(DestroyAPIView):
    serializer_class = None
    queryset = Wishlist.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            wishlist = self.queryset.get(id=pk, user=request.user)
            wishlist.delete()
            return Response({
                "message": "wishlist deleted",
            }, status=status.HTTP_202_ACCEPTED)
        except Wishlist.DoesNotExist:
            return Response({
                "message": "wishlist not found",
            }, status=status.HTTP_404_NOT_FOUND)
        


            
        


