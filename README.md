[![Build Status](https://travis-ci.org/alansvieceli/api-pontos-turisticos.svg?branch=master)](https://travis-ci.org/alansvieceli/api-pontos-turisticos)

# api-pontos-turisticos


python -m venv venv -> criar a virtual env


/*ativar virtual env*/
venv\Scripts\activate

/*desativar virtual env*/
venv\Scripts\deactivate


pip install django
pip install djangorestframework
django-admin startproject api-pontos-turisticos .  (cria um novo projeto django, o ponto é pra nao criar um sub diretório)

python manage.py createsuperuser --email alan.vieceli@gmail.com --username admin    (https://www.django-rest-framework.org/tutorial/quickstart/)


/*https://docs.djangoproject.com/en/2.1/topics/migrations/*/
python manage.py makemigrations
python manage.py migrate

/*inicia o servidor*/
python manage.py runserver

http://127.0.0.1:8000/admin/

-------------------------------------------------------------------------------------------------------------------------------------------

python manage.py startapp core    
python manage.py startapp atracoes
python manage.py startapp comentarios
python manage.py startapp avaliacoes
python manage.py startapp endereco


    - resgistrar no settings.py (project)
    - criar pasta api
    - criar o model no arquivo model.py (app)
    - registrar no admin.py (app)