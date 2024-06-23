FROM postgres:16.3

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=hydrostat_db

RUN chmod a+r /docker-entrypoint-initdb.d/*
