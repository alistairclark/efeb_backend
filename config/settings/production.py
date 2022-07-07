import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from config.settings.base import *


DATABASES["default"] = dj_database_url.config(conn_max_age=600)

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [
    ".herokuapp.com",
]

# AWS S3 SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET")
AWS_S3_REGION_NAME = "eu-west-2"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

sentry_sdk.init(
    dsn="https://e200202f7d8e4c66a73cb3a7ea07a4e7@o1307791.ingest.sentry.io/6552533",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
