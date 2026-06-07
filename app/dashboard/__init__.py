from flask import Blueprint

# ----------- Instiantiate Blueprint ----------- #
dashboard = Blueprint('dashboard', __name__)

from . import routes