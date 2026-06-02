from rest_framework.serializers import ModelSerializer
from apps.book.models import Wishlist, Book
from rest_framework.exceptions import ValidationError

class WishlistCreateSeralzier(ModelSerializer):
    user = None
    class Meta:
        model = Wishlist
        fields = '__all__'

    def validate_book(self, book):
        wishlist = Wishlist.objects.filter(book=book, user=self.user)
        if wishlist.exists():
            raise ValidationError("book already your wishlist")
        return book


class WishlistListSeralzier(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'

