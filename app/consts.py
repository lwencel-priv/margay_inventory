import os

from elasticsearch import AsyncElasticsearch

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
ELASTIC_APM_HOST = "http://"
ELASTIC_APM_PORT = 8200
ELASTIC_APM_CONFIG = {
    "SERVICE_NAME": SERVICE_NAME,
    "SERVER_URL": f"{ELASTIC_APM_HOST}:{ELASTIC_APM_PORT}",
}
