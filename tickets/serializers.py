from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','name','surname','departure','destination','price','departureDateTime','timeFlight')
        model = Ticket


class UserLoggedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        model = get_user_model()
