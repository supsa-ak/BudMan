from rest_framework import generics, status
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import *
from .models import Transaction
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class TransactionView(generics.ListAPIView):
    def get(self, request, format=None):
        serializer_class = TransactionSearializer
        queryset = Transaction.objects.filter(user=request.user)
        dat = []
        for i in queryset:
            dat.append(TransactionSearializer(i).data)
        return Response({'data':dat}, status=status.HTTP_200_OK)

class CreateTransactionView(APIView):
    def post(self, request, format=None):
        if request.user.is_authenticated:
        
            user = request.user
            name = request.data.get('name')
            amount = request.data.get('amount')
            category = request.data.get('category')
            note = request.data.get('note')

            transaction = Transaction(user=user, name=name, amount=amount, category=category, note=note)
            transaction.save()

            return Response(TransactionSearializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response({'message':'Login Required'}, status=status.HTTP_404_NOT_FOUND)

class UpdateTransactionView(APIView):
    def post(self, request, format=None):
        if request.user.is_authenticated:
            id = request.data.get('id')
            
            queryset = Transaction.objects.filter(id=id)
            transaction = queryset[0]
            transaction.name = request.data.get('name')
            transaction.amount = request.data.get('amount')
            transaction.category = request.data.get('category')
            transaction.note = request.data.get('note')
            transaction.save(update_fields=['name','amount','category','note'])

            return Response(TransactionSearializer(transaction).data, status=status.HTTP_200_OK)
        return Response({'message':'Login Required'}, status=status.HTTP_404_NOT_FOUND)


class DeleteTransactionView(APIView):
    def post(self, request, format=None):
        if request.user.is_authenticated:
            id = request.data.get('id')
            
            queryset = Transaction.objects.filter(id=id)
            transaction = queryset[0]
            transaction.delete()

            return Response({'message':'Deleted Successfully'}, status=status.HTTP_200_OK)
        return Response({'message':'Login Required'}, status=status.HTTP_404_NOT_FOUND)