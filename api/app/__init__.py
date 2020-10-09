import logging.config
import os
import sys

from flask import Flask, g

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import uuid

import app.constants as constant
import pika
from app.decorators.restplus import api as api_rest_plus
from celery import Celery
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateSchema


print(os.environ)

"""__________________________________producer for COMPUTE_______________________________________________________"""

class CalculationModuleRpcClient(object):
    def __init__(self):
        parameters = pika.URLParameters(constants.CELERY_BROKER_URL)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=False)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            self.on_response, no_ack=True, queue=self.callback_queue
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, cm_id, data):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key=constants.RPC_Q + str(cm_id),
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=data,
        )
        while self.response is None:
            self.connection.process_data_events()
        return self.response

    def is_calculation_module_alive(self, cm_id):
        self.response = None
        self.corr_id = str(cm_id)
        self.channel.basic_publish(
            exchange="",
            routing_key=constants.RPC_CM_ALIVE,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body="",
        )
        while self.response is None:
            ##print ('Cm with cm id {} is not connected',cm_id)
            self.connection.process_data_events()
        # print ('self.response ',self.response)
        return self.response


dbGIS = SQLAlchemy()

celery = Celery(
    __name__,
    backend=constants.CELERY_RESULT_BACKEND,
    broker=constants.CELERY_BROKER_URL,
)

# methods
log_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "", "logging.conf"
)
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)
# logging.getLogger('flask_cors').level = logging.DEBUG

# Instantiate extra modules
dbGIS = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

def create_db(app, engine):
    """Create the database table if they don't exist yet
    """

def create_app(config_name):
    """
    Create app instance
    """
    app = Flask(__name__)
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    cfg = os.path.join(current_file_dir, "config", config_name + ".py")
    app.config.from_pyfile(cfg)
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    # initialize extensions
    from .api_v1 import api

    api_rest_plus.init_app(api)

    from .api_v1 import nsStats as main_stats_namespace

    api_rest_plus.add_namespace(main_stats_namespace)

    from .api_v1 import nsUsers

    api_rest_plus.add_namespace(nsUsers)

    from .api_v1 import nsUpload

    api_rest_plus.add_namespace(nsUpload)

    from .api_v1 import nsSnapshot

    api_rest_plus.add_namespace(nsSnapshot)

    from .api_v1 import load_profile_namespace as main_heat_load_profile_namespace

    api_rest_plus.add_namespace(main_heat_load_profile_namespace)

    from .api_v1 import nsCM

    api_rest_plus.add_namespace(nsCM)

    from .api_v1 import nsLayers

    api_rest_plus.add_namespace(nsLayers)

    app.register_blueprint(api)
    dbGIS.init_app(app)
    #create non existant tables
    with app.app_context():
        dbGIS.create_all()
    mail.init_app(app)
    login_manager.init_app(app, add_context_processor=False)

    geoserver_cors = os.environ.get("GEOSERVER_URL", "")
    www_cors = os.environ.get("CLIENT_URL", "")

    origins = {geoserver_cors,
              www_cors,
              "http://maps.googleapis.com/"
              "http://maps.googleapis.com/maps/api/geocode/",
              "http://maps.googleapis.com/maps/api/",
              "http://maps.googleapis.com/*",
    }
    if app.debug:
        origins = {'*'}
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": origins
            }
        },
    )
    return app
