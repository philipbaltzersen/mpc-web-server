FROM postgres:16.2

ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB data

COPY init.sql /docker-entrypoint-initdb.d/
