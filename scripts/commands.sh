#!/bin/sh

#Em caso de falha o script é encerrado
set -e

#Comandos de rotina para o container
echo 'Executando comandos internos...' 
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

#Adicionar comando para verificar conexão com o InfluxDB