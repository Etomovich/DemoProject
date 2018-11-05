from flask import Blueprint

bp = Blueprint("api_V1",__name__)

from SendIT_App.api.Version1.views.parcelView import parcels_bp