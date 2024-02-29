FROM python:3.11.3-alpine3.18.2
LABEL mantainer="yano.melo.cavalcante@gmail.com"

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
    /venv/bin/pip isntall --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    chown -R duser:duser /venv && \
    chown -R duser-duser /data/web/static \
    chmod -R 755 /data/web/static && \
    chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

#Troca o usuário do root para o duser
USER duser

CMD ["commands.sh"]