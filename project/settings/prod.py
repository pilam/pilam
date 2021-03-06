from .base import *

# Core
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = [
    '.pilam.com',
    '.herokuapp.com',
]

# Storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SendGrid
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env("SENDGRID_API_KEY")

# Cloudinary
CLOUDINARY_STORAGE = {
    'PREFIX': 'pilam',
}

# Sentry
SENTRY_CONFIG['release'] = env("HEROKU_SLUG_COMMIT")
