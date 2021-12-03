from django.contrib.auth import get_user_model
from django.db import models


class Ticket(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.FloatField()
    departureDateTime = models.DateTimeField()
    arrivalDateTime = models.DateTimeField()

    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}, Departure: {self.departure}, Destination: {self.destination}, Price: {self.price}'
