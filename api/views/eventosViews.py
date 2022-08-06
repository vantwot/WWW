from rest_framework import viewsets
from rest_framework.response import Response
from api.models.eventos import Eventos
from api.serializers import EventosSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer