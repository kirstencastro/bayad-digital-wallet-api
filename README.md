# Digital Wallet API

![Python](https://img.shields.io/badge/Python-3.7-blue)


## Run Locally

To run `digital-wallet-api` locally:

Install dependencies

```bash
  $ pip install -r requirements.txt 
```

Start the server

> Install gunicorn
```bash
  $ pip install gunicorn  # Skip this if already installed gunicorn
```
> Run server
```bash
  $ gunicorn wsgi -w 4 -b 0.0.0.0:5001 --timeout 3000
```

## API Documentation

API Documentation can be found [here](https://documenter.getpostman.com/view/22693892/VUjPGjer).
