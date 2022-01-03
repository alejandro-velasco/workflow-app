FROM python:3-alpine
ADD . /api
WORKDIR /api
RUN mv /api/scripts /scripts

# You will need this if you need PostgreSQL, otherwise just skip this
RUN apk update && \
    apk add postgresql-dev \
    gcc python3-dev musl-dev \
    libffi-dev \
    git
RUN pip install -r requirements.txt && pip install psycopg2
RUN chmod +x /scripts/*
# USER nobody
EXPOSE 8000
CMD ["/scripts/entrypoint.sh"]
