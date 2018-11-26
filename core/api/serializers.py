from rest_framework.serializers import ModelSerializer
from core.models import PontoTurstico


class PontoTursticoSerializer(ModelSerializer):
    class Meta:
        model = PontoTurstico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')
