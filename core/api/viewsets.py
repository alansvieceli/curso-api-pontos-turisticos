from rest_framework.viewsets import ModelViewSet
from core.models import PontoTurstico
from .serializers import PontoTursticoSerializer


class PontoTursticoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTurstico.objects.all()
    serializer_class = PontoTursticoSerializer
