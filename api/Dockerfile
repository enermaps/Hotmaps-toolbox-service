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

#cleanup buid tools
RUN apt-get remove --yes \
    cmake \
    openssh-client \
    build-essential \
    wget \
    gcc \
    perl-modules \
    git \
    ssh



EXPOSE 80

# Copy app source code
ADD ./requirements.txt /api/requirements.txt
RUN pip3 install -r /api/requirements.txt

# copy supervisord service over
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor.conf
COPY local_flask.sh /bin/local_flask

COPY . .

# Start processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.conf"]
