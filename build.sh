#!/bin/bash

# Instala as dependências
pip install -r requiriments.txt

# Executa as migrações do banco de dados
python manage.py migrate

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o servidor da aplicação
python manage.py runserver
