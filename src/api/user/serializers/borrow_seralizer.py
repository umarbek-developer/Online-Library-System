from rest_framework.serializers import ModelSerializer
from apps.book.models import Borrow


class BorrowCreateSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowListSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowUpdateSeralzier(ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'
