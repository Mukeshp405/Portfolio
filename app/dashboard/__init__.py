from flask import Blueprint

# ----------- Instiantiate Blueprint ----------- #
dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/")
def redirect_to_vercel():
    return redirect(
        "https://mukesh-prajapati.vercel.app/",
        code=301
    )

from . import routes
