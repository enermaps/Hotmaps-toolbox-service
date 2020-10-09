from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")
from ..decorators import etag
from .computation_module import nsCM
from .heat_load_profile import load_profile_namespace
from .snapshot import nsSnapshot
from .stats import nsStats
from .upload import nsUpload
from .users import nsUsers
from .layers import nsLayers


@api.before_request
def before_request():
    """All routes in this blue#print require authentication."""
    pass


@api.after_request
@etag
def after_request(rv):
    """Generate an ETag header for all routes in this blue#print."""

    return rv


from . import computation_module

# from . import  computation, errors
