from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import PontoTurstico
from .serializers import PontoTursticoSerializer


class PontoTursticoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    #queryset = PontoTurstico.objects.all()
    #queryset = PontoTurstico.objects.filter(aprovado=True)
    serializer_class = PontoTursticoSerializer

    def get_queryset(self):
        return PontoTurstico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):  #sobescrevendo GET
        return super(PontoTursticoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs): #sobrescrevendo POST
        return super(PontoTursticoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs): #sobrescrevendo DELETE (/código)
        return super(PontoTursticoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs): # sobrescrevendo #sobescrevendo GET (/codigo)
        return super(PontoTursticoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs): # sobrescrevendo #sobescrevendo PUT (/codigo)
        return super(PontoTursticoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs): # sobrescrevendo #sobescrevendo PATCH (/codigo) (atualziando o parialmente o update)
        return super(PontoTursticoViewSet, self).partial_update(request, *args, **kwargs)

    #implementando nossas proprias actions
    @action(methods=['get'], detail=True) # http://127.0.0.1:8000/pontosturistico/2/denunciar/
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)  # http://127.0.0.1:8000/pontosturistico/teste/
    def teste(self, request):
        pass
