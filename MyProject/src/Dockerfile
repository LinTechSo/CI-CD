FROM ubuntu:latest

WORKDIR "/srv"

RUN apt-get update && \
        apt-get upgrade -y

RUN apt-get update && apt-get install -y python3 python3-pip python3-dev build-essential \
        && apt-get install mysql-server libmysqlclient-dev -y 

COPY ./requirements.txt /srv/requirements.txt

RUN pip3 install -r requirements.txt    

COPY . /srv

CMD [ "uwsgi", "--socket", "0.0.0.0:5000", \
               "--protocol", "http", \
               "-w", "wsgi:app" ]
