FROM mysql:5.7

COPY ./user.sql /docker-entrypoint-initdb.d/user.sql

 RUN chown mysql:mysql /docker-entrypoint-initdb.d/*.sql

CMD ["docker-entrypoint.sh", "mysql"]