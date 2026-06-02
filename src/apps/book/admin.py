from django.contrib import admin
from apps.book.models import Book, Borrow, Wishlist

# Register your models here.

admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Wishlist)
