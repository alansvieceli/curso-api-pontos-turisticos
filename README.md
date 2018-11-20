[![Build Status](https://travis-ci.org/alansvieceli/api-pontos-turisticos.svg?branch=master)](https://travis-ci.org/alansvieceli/api-pontos-turisticos)

# api-pontos-turisticos


python -m venv venv -> criar a virtual env


/*ativar virtual env*/
venv\Scripts\activate

/*desativar virtual env*/
venv\Scripts\deactivate


pip install django
django-admin startproject api-pontos-turisticos .  (cria um novo projeto django, o ponto é pra nao criar um sub diretório)

python manage.py createsuperuser --email admin@example.com --username admin    (https://www.django-rest-framework.org/tutorial/quickstart/)


/*https://docs.djangoproject.com/en/2.1/topics/migrations/*/
manage.py makemigrations
manage.py migrate

/*inicia o servidor*/
manage.py runserver

http://127.0.0.1:8000/admin/

-------------------------------------------------------------------------------------------------------------------------------------------

python manage.py startapp pontos_turisticos
python manage.py startapp atracoes
python manage.py startapp comentarios
python manage.py startapp avaliacoes
python manage.py startapp endereco