from rest_framework import serializers
from api.models.eventos import Eventos

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = 'id', 'title', 'description'
