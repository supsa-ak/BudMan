from rest_framework import serializers
from .models import Transaction

class TransactionSearializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'created', 'name', 'amount', 'category', 'note')

# class CreateTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ('user', 'name', 'amount', 'category', 'note')

# class UpdateTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ('id', 'name', 'amount', 'category', 'note')