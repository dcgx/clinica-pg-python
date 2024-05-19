import psycopg2

from db import config

def get_connection():
    return psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )