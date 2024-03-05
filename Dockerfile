FROM python:3.11.8-alpine3.18
LABEL maintainer="yano.melo.cavalcante@gmail.com"

#Gravação de arquivos bytecode?
ENV PYTHONDONTWRITEBYTECODE 1

#Buffer
ENV PYTHONUNBUFFERED 1

#Cópia dos Arquivos para o container -> [origem | container]
COPY djangoapp /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser

ENV PATH="/scripts:/venv/bin:$PATH"

#Troca o usuário do root para o duser
USER duser

CMD ["commands.sh"]