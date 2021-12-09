from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from tickets.validators import validate_len, validate_price, validate_current_date, validate_limit_min_time


class Ticket(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, validators=[validate_len, RegexValidator(r'^[A-Z][a-z]*(?:\s[A-Z][a-z]*)*$')])
    surname = models.CharField(max_length=50, validators=[validate_len, RegexValidator(r'^[A-Z][a-z]*(?:\s[A-Z][a-z]*)*$')])
    departure = models.CharField(max_length=50, validators=[validate_len, RegexValidator(r'^[A-Z][a-z]*(?:\s[A-Z][a-z]*)*$')])
    destination = models.CharField(max_length=50,validators=[validate_len, RegexValidator(r'^[A-Z][a-z]*(?:\s[A-Z][a-z]*)*$')])
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[validate_price])
    departureDateTime = models.DateTimeField(validators=[validate_current_date])
    timeFlight = models.TimeField(validators=[validate_limit_min_time])

    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}, Departure: {self.departure}, Destination: {self.destination}, Price: {self.price}'

'''
    def clean(self):
        validate_date(self.departureDateTime, self.arrivalDateTime)

    def save(self, *args, **kwargs):
        self.clean()
        super(Ticket,self).save(*args, **kwargs)

    
    def save(self, *args, **kwargs):
        #self.clean()
        return super().save(*args, **kwargs)'''