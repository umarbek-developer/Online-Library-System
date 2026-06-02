from rest_framework.serializers import ModelSerializer
from apps.book.models import Book


class BookCreateSeralzier(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookListSeralzier(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSeralzier(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'published_date', 'borrows_count', 'published_user', 'deleted_by']
