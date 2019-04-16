# Ingresse

Este projeto serve para gerenciar usuários.

## Configuração

Este projeto utilizou os seguintes componentes:

- Python
- Flask
- Docker
- PostgreSQL

## Execução

Para executar a aplicação siga as seguintes etapas:

- Digite `docker-compose up --build`.
- Digite `docker-compose exec app python manage.py db init`
- Digite `docker-compose exec app python manage.py db migrate`
- Digite `docker-compose exec app python manage.py db upgrade`
- Digite `docker-compose exec app python manage.py seed`

## Testes

Para testar a aplicação digite `docker-compose exec app python manage.py test` ou
`docker-compose exec app python manage.py test --coverage` para gerar relatório de abrangência
de testes.
