#!/bin/sh
uvicorn app.asgi:application --reload --host 0.0.0.0 --port ${PORT:-8000}
