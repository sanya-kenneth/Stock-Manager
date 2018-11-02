from urllib.parse import urlparse
import psycopg2
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
        self.cursor = self.con.cursor()

    def create_tables(self):

        commands = (
        """
        CREATE TABLE IF NOT EXISTS user_table(
        userid SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        useremail TEXT NOT NULL,
        userpassword TEXT NOT NULL,
        adminstatus BOOL NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS product_table(
        productid SERIAL PRIMARY KEY,
        productname VARCHAR(50) NOT NULL,
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
        productid INT NOT NULL,
        productname VARCHAR(50) NOT NULL,
        productquantity INT NOT NULL,
        TOTAL INT NOT NULL,
        saledate TEXT NOT NULL
        )
        """
        )
      
        for com in commands:
            self.cursor.execute(com)
  
    def select_users(self):
        sql = ("""SELECT * from user_table """)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
       
    def select_a_user(self,user_email_in):
        sql = ("""SELECT * from user_table WHERE useremail = '{}'""".format(user_email_in))
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def select_products(self):
        sql = ("""SELECT * from product_table """)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_a_product(self,product_id_in):
        sql = ("""SELECT * from product_table WHERE productid = {} """.format(product_id_in))
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def update_product(self,product_id_in,product_name_in,product_quantity_in,product_price_in,product_description_in):
         
        sql = ("""UPDATE product_table SET productname = '{}',productquantity = '{}',
        productprice = '{}', productdescription = '{}' WHERE productid = '{}' """\
         .format(product_name_in, product_quantity_in, product_price_in,product_description_in,product_id_in))
        self.cursor.execute(sql)
        return True
               
    def delete_product(self,product_id):
        sql = ("""DELETE from product_table WHERE productid = '{}' """.format(product_id))
        self.cursor.execute(sql)
        return True

    def select_sales(self):
        sql = ("""SELECT * from sales_table """)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
       
    def select_sale(self,sale_id):
        sql = ("""SELECT * from sales_table WHERE saleid = '{}' """.format(sale_id))
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def update_quantity(self,product_id_in,product_quantity_in):
        sql = ("""UPDATE product_table SET productquantity = '{}' WHERE productid = '{}'""".format(product_quantity_in,product_id_in))
        self.cursor.execute(sql)
        return True

db = Database('postgres://postgres:psql@localhost:5432/store')
