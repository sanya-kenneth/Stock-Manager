from app.auth.database import db_handler


class Sale:
    """
    Class for creating the sale object

    :params  attedt_id, attedt_name, product_name, product_quantity, product_price, Total, sale_date:
    """
    def __init__(self,attedt_id, attedt_name, product_name, product_quantity, product_price, Total, sale_date):
        self.attedt_id = attedt_id
        self.attedt_name = attedt_name
        self.product_id = product_name
        self.product_name = product_quantity
        self.product_quantity = product_price
        self.Total = Total
        self.sale_date = sale_date

    def add_sale(self):
        sql = ("""INSERT INTO sales_table(attendantid,attendantname,productid,productname,
        productquantity,Total,saledate) VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(self.attedt_id,\
        self.attedt_name,self.product_id,self.product_name,self.product_quantity,self.Total,self.sale_date))
        db_handler().cursor.execute(sql)