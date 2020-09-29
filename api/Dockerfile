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
# Copy app source code
ADD ./requirements.txt /api/requirements.txt
RUN pip3 install -r /api/requirements.txt
COPY . .
COPY local_flask.sh /bin/local_flask

#cleanup buid tools
RUN apt-get remove --yes \
    python-numpy \
    cmake \
    openssh-client \
    build-essential \
    wget \
    gcc \
    perl-modules \
    git \
    ssh &&  \
    apt-get autoremove --yes



EXPOSE 80

# copy supervisord service over
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor.conf

# Start processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.conf"]
