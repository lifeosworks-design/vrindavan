#!/usr/bin/env bash
# Production start for Render (or any host): seed sample data, create the admin, serve with waitress.
set -e
flask --app run seed
if [ -n "$VR_ADMIN_EMAIL" ] && [ -n "$VR_ADMIN_PASSWORD" ]; then
  flask --app run create-admin --email "$VR_ADMIN_EMAIL" --password "$VR_ADMIN_PASSWORD" || true
fi
exec waitress-serve --listen=0.0.0.0:${PORT:-8000} run:app
