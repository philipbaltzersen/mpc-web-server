FROM postgres:16.2

COPY .db-password /run/secrets/db_password

ENV POSTGRES_PASSWORD_FILE = /run/secrets/db_password

COPY init.sql /docker-entrypoint-initdb.d/
