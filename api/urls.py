from django.urls import path
from .views import *

urlpatterns = [
    path('', TransactionView.as_view()),
    path('create-transaction', CreateTransactionView.as_view()),
    path('update-transaction', UpdateTransactionView.as_view()),
    path('delete-transaction', DeleteTransactionView.as_view()),
]