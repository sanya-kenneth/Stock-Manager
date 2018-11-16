import datetime
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.auth.database import db_handler


class Product:
    """
    Class for creating the product object

    :params  product_name,product_quantity,product_price,product_description:
    """
    def __init__(self,product_name,product_quantity,product_price,product_description):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_description = product_description
        self.date_added = datetime.datetime.now()


    def add_product(self):
        sql = ("""INSERT INTO product_table(productname, productquantity, productprice,productdescription,dateadded) VALUES ('{}','{}','{}','{}','{}')""" \
        .format(self.product_name, self.product_quantity, self.product_price, self.product_description, self.date_added))
        db_handler().cursor.execute(sql)
        return True