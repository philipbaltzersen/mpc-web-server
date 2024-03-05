FROM postgres:16.2

COPY .db-password /run/secrets/db-password

ENV POSTGRES_PASSWORD_FILE = /run/secrets/db-password

COPY init.sql /docker-entrypoint-initdb.d/
