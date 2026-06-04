from rest_framework.serializers import ModelSerializer
from apps.book.models import Borrow, Book, BookStatus
from rest_framework.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone

class BorrowCreateSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted', 'deleted_by']
    

    def validate_returned_time(self, obj):
        now = timezone.now()
        ertaga = now + timedelta(days=1)
        uzoq_muddat = now + timedelta(days=180)
        if ertaga.date() > obj.date():
            raise ValidationError("Kitobni olish vaqti kamida 1 kundan uzoq muddat bo'lishi kerak.")
        elif uzoq_muddat.date() < obj.date():
            raise ValidationError("Maximal 180 kunlik muddatga ololasiz holos.")
        return obj
    
    def validate_book(self, obj):
        if obj.status != BookStatus.FREE:
            raise ValidationError("Kitob bron qilingan.")
        return obj
    



class BorrowListSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowUpdateSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted', 'getting_time', 'book', 'user', 'deleted_by']


    def validate_returned_time(self, obj):
        now = timezone.now()
        ertaga = now + timedelta(days=1)
        uzoq_muddat = now + timedelta(days=180)
        if ertaga.date() > obj.date():
            raise ValidationError("Kitobni olish vaqti kamida 1 kundan uzoq muddat bo'lishi kerak.")
        elif uzoq_muddat.date() < obj.date():
            raise ValidationError("Maximal 180 kunlik muddatga ololasiz holos.")
        return obj