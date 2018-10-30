from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as pg_extra
from flask import current_app as app





class Database():
    """
    This class connects the app to the database
    """
    def __init__(self,Database_url):
        parsed_url = urlparse(Database_url)
        db = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port

        self.con = psycopg2.connect(database=db,user=username,password=password,host=hostname, port=port)
        self.con.autocommit = True
        self.c = self.con.cursor()
        print("you are connected to the database")

db = Database('postgres://postgres@localhost/store')
db.create_table()



# app.config(['DATABASE_URL'])
# 'postgres://postgres@localhost/store'