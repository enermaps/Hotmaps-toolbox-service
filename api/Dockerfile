FROM hotmaps/base_cm:latest

ENV CELERY_BROKER_URL amqp://admin:mypass@rabbit:5672/
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# setup volume
RUN mkdir -p /data
VOLUME /data

RUN mkdir -p /var/hotmaps/users

# Setup app server
WORKDIR /api
COPY . .
COPY flask.sh /bin/local_flask

# Copy app source code
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 && \
    pip3 install -r requirements.txt

EXPOSE 80

# copy supervisord service over
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start processes
CMD ["/usr/bin/supervisord"]
