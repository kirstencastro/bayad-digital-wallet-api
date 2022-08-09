"""Pseudo handler for wallet model."""


# Using this list as a mock database of wallet accounts
wallets = [
    {"wallet_id": 1, "balance": 100},
    {"wallet_id": 2, "balance": 23023},
    {"wallet_id": 3, "balance": 45700},
]


class Wallet:
    """Holds functions for mocking a wallet database."""

    def __init__(self):
        self.wallets = wallets

    def get_wallet(self, wallet_id: int):
        """Returns a wallet from the `wallets` list if it exists.

        :param id: Refers to the index of the items in the `wallets` list
        :type id: int

        :return: dictionary of wallet data
        :rtype: dict or None
        """

        # we deduct 1 from the id argument to simulate actual id values
        # i.e. starts with 1
        wallet_id -= 1

        try:
            wallet = wallets[wallet_id]
        except IndexError:
            return None
        else:
            return wallet
