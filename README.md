# Rotten Potatoes 🍠
Desafio Backend da Fábrica de Software Unipe 2025.1

## Sobre o App
Semelhante ao renomado site Rotten Tomatoes, o aplicativo poderá consultar filimes pelo título assim o usuário poderá ver informações da obra

## Documentações adicionais
- [Python](https://www.python.org/doc/)
- [Django](https://docs.djangoproject.com) 
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com/reference/cli/docker/)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## API externa
    
- [OMDb API The Open Movie Database](http://www.omdbapi.com/)

## Funcionalidades

- **Consulta de Filmes**: Permite buscar informações sobre filmes utilizando a API OMDB.
- **CRUD de Filmes**: Permite criar, listar, atualizar e deletar filmes no banco de dados.
- **CRUD de Reviews**: Permite criar, listar, atualizar e deletar reviews de filmes.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

    wsBackend-Fabrica25.1/
    ├── app_rotten_potatoes/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── serializers.py
    │   │   ├── urls.py
    │   │   ├── viewsets.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   ├── __init__.py
    │   │   └── ... (migration files)
    │   ├── models.py
    │   ├── tests.py
    │   ├── utils.py
    │   ├── views.py
    ├── manage.py
    ├── project_rotten_potatoes/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── venv/
    │   ├── bin/
    │   ├── include/
    │   ├── lib/
    │   ├── ... (virtual environment files)
    └── requirements.txt

## Requisitos

- Python 3.11
- Django 5.1.6
- Django REST framework 3.15.2

## Instalação

1. Clone o repositório:
```sh
git clone <URL_DO_REPOSITORIO>
cd wsBackend-Fabrica25.1
```

Crie e ative um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

Instale as dependências:
```sh
pip install -r requirements.txt
```

Execute as migrações:
```sh
python manage.py migrate
```

Inicie o servidor de desenvolvimento:
```sh
python manage.py runserver
```

## Endpoints

### Filmes

- `GET /api/movies/`: Lista todos os filmes.
- `POST /api/movies/create/`: Cria um novo filme.
- `GET /api/movies/<id>/`: Recupera um filme específico.
- `PUT /api/movies/<id>/update/`: Atualiza um filme específico.
- `DELETE /api/movies/<id>/delete/`: Deleta um filme específico.

### Reviews

- `GET /api/reviews/`: Lista todas as reviews.
- `POST /api/reviews/create/`: Cria uma nova review.
- `GET /api/reviews/<id>/`: Recupera uma review específica.
- `PUT /api/reviews/<id>/update/`: Atualiza uma review específica.
- `DELETE /api/reviews/<id>/delete/`: Deleta uma review específica.

## Docker

Para construir e rodar o projeto utilizando Docker, execute os seguintes comandos:

```sh
sudo docker build -t app_rotten_potatoes .
sudo docker run -d -p 8000:8000 app_rotten_potatoes
```