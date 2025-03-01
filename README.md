<!-- Esse markdown não foi automaticamente gerado por IA  -->
<!-- É fruto de estilização humana -->

# Rotten Potatoes 🍠
Desafio Backend da Fábrica de Software Unipe 2025.1

## Sobre o App
Semelhante ao renomado site Rotten Tomatoes, o aplicativo poderá consultar filimes pelo título por uma API. Assim o usuário poderá ver informações sobre a obra.
Também é possível fazer operações de CRUD (Create, read, update and delete) com os Filmes, desde que ele exista na API externa.
Além disso, o usuário pode até fazer uma review com nota, contanto que o filme já esteja registrado em nossa API, e operações CRUD consequentemente.

## Sobre o desenvolvimento
O projeto foi desenvolvido inteiramente em ambiente **linux** usando a distribuição **NixOS**, todas as ferramentas utilizadas no projeto foram declaradas no arquivo de configurações em `/etc/nixos/` e devidamente instaladas (*firefox, git, vscode, python, docker, docker-compose, vim, neovim*) feitas essa semana.

Fora a IDE **(vscode)** e o navegador **(firefox)**, nenhuma outra interface gráfica foi utilizada (*github desktop, postman, etc*) comandos do **git** foram rodados no **terminal** e inclusive o **neovim** foi utilizado como editor de texto algumas vezes para pequenas edições. Os testes da API foram feitos manualmente na própria interface fornecida pelo próprio **Django Rest Framework**.

No momento em que se inciou o desenvolvimento do desafio, eu tinha uma boa noção de *python, git, estrutura de projeto, POO*. Alguma noção de *django e rest api*. Porem nenhuma noção de *docker, docker-compose, postgres, autentificação e templates*.
Estudei os materiais que tinha a disposição, procurei nas documentações, questionei as IAs (*ChatGPT, Copilot*) para entender melhor como fazer os requisitos extras, consegui realizar a parte do banco de dados externo e do docker-compose, mas ficou faltando autentificação e uso de templates, fica como aprendizado para o futuro.

## Documentações
- [Git](https://git-scm.com/doc)
- [Python](https://www.python.org/doc/)
- [Django](https://docs.djangoproject.com) 
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com/reference/cli/docker/)
- [PostgreSQL](https://www.postgresql.org/docs/)

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![NixOS](https://img.shields.io/badge/NIXOS-5277C3.svg?style=for-the-badge&logo=NixOS&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)
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
    ├── docker-compose.yml
    ├── dockerfile
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
- Requests 2.32.3
- psycopg 3.2.5

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

## Docker Compose

Para construir e rodar o projeto utilizando Docker-compose e com integração ao PostgreSQL, execute os seguintes comandos:

```sh
    sudo docker-compose run web python manage.py makemigrations
    sudo docker-compose run web python manage.py migrate
    sudo docker-compose up
```

## Endpoints

### Filmes

- `GET /api/movies/`: Lista todos os filmes.
- `GET /api/movies?title=<title>` Busca filme pelo titulo na OMDb API
- `POST /api/movies/create/`: Cria um novo filme.
- `GET /api/movies/<id>/`: Recupera um filme específico.
- `PUT /api/movies/<id>/update/`: Atualiza um filme específico.
- `DELETE /api/movies/<id>/delete/`: Deleta um filme específico.

### Reviews

- `GET /api/reviews/`: Lista todas as reviews.
- `GET /api/reviews?movie=<id>`: Lista todas as reviews de um filme pelo seu ID
- `POST /api/reviews/create/`: Cria uma nova review.
- `GET /api/reviews/<id>/`: Recupera uma review específica.
- `PUT /api/reviews/<id>/update/`: Atualiza uma review específica.
- `DELETE /api/reviews/<id>/delete/`: Deleta uma review específica.

## Rodando o Server com Metodos Legado

Devido alterações em `project_rotten_potatoes/settings.py` as formas de fazer rodar o servidor feitas posteriormente so funcionam se alterarmos o banco de dados de postgres para db.sqlite3 novamente

Em `settings.py` faça a seguinte alteração em DATABASES
```py 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.db.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
A alteração já vai estar comentada, só é preciso retirar o comentário e comentar a outra opção de DATABASES.

### Localmente (Legado)

Provavelmente será necessário executar makemigrations:
```sh
python manage.py makemigrations
```

Execute as migrações:
```sh
python manage.py migrate
```

Inicie o servidor de desenvolvimento:
```sh
python manage.py runserver
```

### Docker (Legado)

Para construir e rodar o projeto utilizando Docker, execute os seguintes comandos:

```sh
sudo docker build -t app_rotten_potatoes .
sudo docker run -d -p 8000:8000 app_rotten_potatoes
```

### Material Auxiliar
- [Linux Commands Cheat Sheet](https://www.geeksforgeeks.org/linux-commands-cheat-sheet/)
- [Materiais de aula e estudo do workshop](https://github.com/beaalmeidas/WorkshopFabrica25.1)
- [Repositório proprio com instruções sobre git](https://github.com/lucas-lucena/hello-git)
- [Estrutura Básica de um Projeto em Django ](https://youtu.be/4u0aI-90KnU)
- [Django Rest Framework for Beginners - Simple CRUD API ](https://youtu.be/OJdFj5hPAKs)
- [Setting up PostgreSQL database with a Django Docker application](https://youtu.be/610jg8bK0I8)
- [Padrões de commits 📜](https://github.com/iuricode/padroes-de-commits)
- [Markdown Badges](https://github.com/Ileriayo/markdown-badges)
- [NixOS packages search](https://search.nixos.org/packages)
- [NixOS Manual](https://nixos.org/manual/nixos/stable/)

