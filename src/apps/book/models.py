from django.db import models
from apps.users.models import User

# Create your models here.

class BookStatus(models.TextChoices):
    BORROWED = 'borrowed', 'Ijaraga olingan.'
    FREE = 'free', 'Bo\'sh.'

class Book(models.Model):
    name = models.CharField(max_length=100)
    published_user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100)
    pages_count = models.IntegerField(default=0)
    borrows_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=BookStatus.choices, default=BookStatus.FREE)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.published_user.get_full_name()}"
    

class BorrowStatus(models.TextChoices):
    RETURNED = 'returned', 'Qaytarilgan.'
    READING = 'reading', 'O\'qilmoqda...'
    EXPIRED = 'expired', 'muddatdan o\'tib ketgan'


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    getting_time = models.DateTimeField(auto_now_add=True)
    returned_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=BorrowStatus.choices, default=BorrowStatus.READING)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.book.name}"
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} | {self.book.name}"
    
