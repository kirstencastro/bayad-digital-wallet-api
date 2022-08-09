"""Created by Kirsten Castro on August 8, 2022."""


def validate(data):
    """Validate request data.

    :param data: data from requests
    """

    try:
        float(data["amount"])
    except KeyError:
        return False

    return True
