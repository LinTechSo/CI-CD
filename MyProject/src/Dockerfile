FROM alpine:3.7

EXPOSE 5000

VOLUME /usr/src/app/public

WORKDIR /usr/src/app

RUN apk add --no-cache \
        uwsgi-python3 \
        python3
        
COPY . .

RUN rm -rf public/*


RUN pip3 install --no-cache-dir -r requirements.txt



CMD [ "uwsgi", "--socket", "0.0.0.0:5000", \
               "--protocol", "http", \
               "--wsgi", "wsgi:app" ]