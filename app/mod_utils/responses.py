"""Created by Kirsten Castro on August 8, 2022."""

from flask_restful import original_flask_make_response as make_response


def generic_404():
    return make_response(
        {"error": "Not Found", "error_code": "NOT_FOUND", "success": False},
        404,
    )


def generic_400():
    return make_response(
        {
            "error": "Bad Request",
            "error_code": "BAD_REQUEST",
            "success": False,
        },
        400,
    )
