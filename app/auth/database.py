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

    def create_tables(self):

        commands = (
        """
        CREATE TABLE IF NOT EXISTS user_table(
        userid SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        useremail TEXT NOT NULL,
        userpassword TEXT NOT NULL,
        adminstatus BOOL NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS product_table(
        productid SERIAL PRIMARY KEY,
        productname TEXT NOT NULL,
        productquantity INT NOT NULL,
        productprice INT NOT NULL,
        productdescription TEXT NOT NULL,
        dateadded TEXT NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS sales_table(
        saleid SERIAL PRIMARY KEY,
        attendantid INT NOT NULL,
        attendantname VARCHAR(50) NOT NULL,
        productname VARCHAR(50) NOT NULL,
        productquantity INT NOT NULL,
        TOTAL INT NOT NULL,
        saledate TEXT NOT NULL
        )
        """
        )
      
        for com in commands:
            self.c.execute(com)

  
    def select_users(self):
        sql = ("""SELECT * from user_table """)
        self.c.execute(sql)
        rows = self.c.fetchall()
        return rows
    
    def select_a_user(self,user_id_in):
        sql = ("""SELECT * from user_table WHERE userid = {} """.format(user_id_in))
        self.c.execute(sql)
        row = self.c.fetchone()
        return row

db = Database('postgres://postgres:psql@localhost:5432/store')

# db = Database('postgres://postgres:psql@localhost:5432/store')
# db.create_tables()



# app.config(['DATABASE_URL'])
# 'postgres://postgres@localhost/store'