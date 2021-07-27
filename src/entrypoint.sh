#!/bin/sh
gunicorn --workers=4 --bind=0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:app --access-logfile=-
