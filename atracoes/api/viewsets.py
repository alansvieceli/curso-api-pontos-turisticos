#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    '''
    https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    
    Caso queira configurar view por view..só tirar do settings:
    
    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    }
    
    filter_backends = (DjangoFilterBackend,) 
    '''

    filter_fields = ('nome', 'descricao')
