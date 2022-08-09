"""Created by Kirsten Castro on August 8, 2022."""

from flask import Flask
from flask_restful import Api

from app.mod_wallet.controllers import BalanceInquiry, CashIn, Debit


def create_app():
    """Initializion for a Flask application."""

    new_app = Flask(__name__)
    api = Api(new_app)

    api.add_resource(BalanceInquiry, "/wallet/<int:id>/balance-inquiry")
    api.add_resource(Debit, "/wallet/<int:id>/debit")
    api.add_resource(CashIn, "/wallet/<int:id>/cash-in")

    return new_app
