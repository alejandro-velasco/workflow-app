FROM python:3-alpine
ADD . /api
WORKDIR /api

ENV KEYFILE_PATH=/data/keys
ENV GIT_REPOSITORY_PATH=/data/git_repos

RUN mv /api/scripts /scripts

# You will need this if you need PostgreSQL, otherwise just skip this
RUN apk update && \
    apk add postgresql-dev \
    gcc python3-dev musl-dev \
    libffi-dev \
    git

RUN pip install -r requirements.txt && pip install psycopg2 && \
    chmod +x /scripts/* && \
    mkdir /git_repos && \
    python3 manage.py makemigrations

# USER nobody
EXPOSE 8000
CMD ["python3", "/scripts/entrypoint.py"]
