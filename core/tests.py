from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class PontoTuristicoTests(APITestCase):

    url_default = '/pontoturistico/'
    url_cod_01 = '/pontoturistico/1/'

    def test_get_page_status_code(self):
        response = self.client.get(self.url_default)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_page_status_code(self):
        data = {'nome': 'Ponto 01', 'descricao': 'Terceiro ponto criado'}
        response = self.client.post(self.url_default, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        '''
                verificar se a parada existe
        '''
        response = self.client.get(self.url_cod_01)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_semalor_page_status_code(self):
        response = self.client.get(self.url_cod_01)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_status_code(self):
        data = {'nome': 'Ponto 01', 'descricao': 'Terceiro ponto criado'}
        response = self.client.post(self.url_default, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        '''
                        verificar se a parada existe
        '''
        response = self.client.get(self.url_cod_01)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        '''
                        alerar algma coisa
        '''
        data = {'nome': 'Ponto 01', 'descricao': 'TerceiroXX ponto criado'}
        response = self.client.put(self.url_cod_01, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_status_code(self):
        data = {'nome': 'Ponto 01', 'descricao': 'Terceiro ponto criado'}
        response = self.client.post(self.url_default, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        '''
                        verificar se a parada existe
        '''
        response = self.client.get(self.url_cod_01)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        '''
                        delete
        '''
        response = self.client.delete(self.url_cod_01)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
