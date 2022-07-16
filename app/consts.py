import os


# APP
SERVICE_NAME = "inventory"
SERVICE_HOST = "0.0.0.0"
SERVICE_PORT = 5001

# ElasticSearch
ELASTIC_AUTH_CONFIG = {
    "hosts": os.environ.get("ELASTIC_HOSTS", "https://es01:9200").split(","),
    "basic_auth": (os.environ.get("ELASTIC_USER", "elastic"), os.environ.get("ELASTIC_PASSWORD", "elastic")),
    "verify_certs": False,
}

# Elastic APM
ELASTIC_APM_CONFIG = {
    "SERVICE_NAME": SERVICE_NAME,
    "SERVER_URL": os.environ.get("ELASTIC_APM_HOST"),
    "SECRET_TOKEN": os.environ.get("ELASTIC_APM_SECRET_TOKEN"),
    "VERIFY_SERVER_CERT": os.environ.get("ELASTIC_APM_VERIFY_SERVER_CERT", False),
}
