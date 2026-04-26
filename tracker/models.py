from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Expense(models.Model):

    TITLE_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Rent', 'Rent'),
        ('Electricity Bill', 'Electricity Bill'),
        ('Internet', 'Internet'),
        ('Movie', 'Movie'),
        ('Gym', 'Gym'),
    ]

    CATEGORY_CHOICES = [
        ('Daily', 'Daily'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    amount = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    



    
