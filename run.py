"""Created by Kirsten Castro on August 8, 2022."""

from app import create_app

app = create_app()
if __name__ == "__main__":
    app.run(port=5002, host="0.0.0.0")
