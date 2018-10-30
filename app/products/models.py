import datetime
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.auth.database import Database


class Product(Database):
    """
    Class for creating the product object

    :params  product_name,product_quantity,product_price,product_description:
    """
    def __init__(self,product_name,product_quantity,product_price,product_description):
        Database.__init__(self,'postgres://postgres:psql@localhost:5432/store')
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_description = product_description
        self.date_added = datetime.datetime.now()


    def add_product(self):
        sql = ("""INSERT INTO product_table(productname, productquantity, productprice,productdescription,dateadded) VALUES ('{}','{}','{}','{}','{}')""" \
        .format(self.product_name, self.product_quantity, self.product_price, self.product_description, self.date_added))
        self.c.execute(sql)
        return True

    def select_products(self):
        sql = ("""SELECT * from product_table """)
        self.c.execute(sql)
        rows = self.c.fetchall()
        return rows

    def select_a_product(self,product_id_in):
        sql = ("""SELECT * from product_table WHERE productid = {} """.format(product_id_in))
        self.c.execute(sql)
        row = self.c.fetchone()
        return row

    def update_product(self,product_id_in,product_name_in,product_quantity_in,product_price_in,product_description_in):
            try:
                sql = ("""UPDATE product_table SET productname = '{}',productquantity = '{}',
                productprice = '{}', productdescription = '{}' WHERE productid = '{}' """.format(product_name_in,product_quantity_in,\
                product_price_in,product_description_in,product_id_in))
                self.c.execute(sql)
                return True
            except:
                return False
    
    def delete_product(self,product_id):
        sql = ("""DELETE from product_table WHERE productid = '{}' """.format(product_id))
        self.c.execute(sql)
        return "deleted"






