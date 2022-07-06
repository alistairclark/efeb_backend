from config.settings.base import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [
    ".herokuapp.com",
]

# AWS S3 SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET")
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
