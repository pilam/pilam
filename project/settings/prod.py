from .base import *

# Core
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = [
    '.pilam.com',
    '.herokuapp.com',
]

# SendGrid
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env("SENDGRID_API_KEY")

# Sentry
# SENTRY_CONFIG['release'] = env("HEROKU_SLUG_COMMIT")

# Cloudinary
CLOUDINARY_STORAGE = {
    'PREFIX': 'pilam',
}
