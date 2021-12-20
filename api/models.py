from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(default=now, editable=True)
    name = models.CharField(max_length=500)
    amount = models.IntegerField()
    categories = [
        ('Rent', 'Rent'),
        ('Travel', 'Travel'),
        ('Investment', 'Investment'),
        ('Shopping', 'Shopping'),
        ('Learning', 'Learning'),
        ('Fees', 'Fees'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=10, default='oth', choices=categories)
    note = models.TextField()

    def __str__(self):
        return (str(self.user) + ' ' + str(self.amount))