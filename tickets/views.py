from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.permissions import IsAuthorOrReadOnly
from tickets.serializers import TicketSerializer

'''
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer'''


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            aut = serializer.validated_data['author']
            if aut == request.user:
                value = serializer.save()
                serializerN = TicketSerializer(value)
                return Response(serializerN.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            aut = serializer.validated_data['author']
            if aut == request.user:
                value = serializer.save()
                serializerN = TicketSerializer(value)
                return Response(serializerN.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
