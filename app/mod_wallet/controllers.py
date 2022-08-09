""""Created by Kirsten Castro on August 8, 2022.

API resources for wallet.

"""

import json
from app.mod_utils.responses import generic_400, generic_404
from app.mod_utils.validation import validate

from flask import request
from flask_restful import Resource
from flask_restful import original_flask_make_response as make_response

from app.mod_wallet.model import Wallet

model = Wallet()


class BalanceInquiry(Resource):
    """Defines resources for fetching balance information."""

    def get(self, id):
        """Get method for balance inquiry."""

        wallet = model.get_wallet(id)

        if wallet is None:
            return generic_404()

        return make_response(
            json.dumps({"balance": wallet["balance"]}),
            200,
            {"Content-Type": "application/json"},
        )


class Debit(Resource):
    """Defines resources for debiting to wallets."""

    def put(self, id):
        """Put method for debiting to existing wallets."""

        data = request.get_json()

        is_valid = validate(data)
        wallet = model.get_wallet(id)

        if wallet is None:
            return generic_404()

        if not is_valid:
            return generic_400()

        wallet["balance"] -= float(data["amount"])
        return make_response(
            json.dumps(wallet), 200, {"Content-Type": "application/json"}
        )


class CashIn(Resource):
    """Defines resources for adding amount to wallets."""

    def put(self, id):
        """Put method for cashing in to existing wallets."""

        data = request.get_json()

        is_valid = validate(data)
        wallet = model.get_wallet(id)

        if wallet is None:
            return generic_404()
        if not is_valid:
            return generic_400()

        wallet["balance"] += float(data["amount"])
        return make_response(
            json.dumps(wallet), 200, {"Content-Type": "application/json"}
        )
