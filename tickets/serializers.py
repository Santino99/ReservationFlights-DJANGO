from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','name','surname','departure','destination','price','departureDateTime','timeFlight')
        model = Ticket
