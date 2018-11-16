from app.auth.database import db_handler


class Sale:
    """
    Class for creating the sale object

    :params  attedt_id, attedt_name, product_name, product_quantity, product_price, Total, sale_date:
    """
    def __init__(self,*args,**kwargs):
        self.attedt_id = args[0]
        self.attedt_name = args[1]
        self.product_id = args[2]
        self.product_name = args[3]
        self.product_quantity = args[4]
        self.Total = args[5]
        self.sale_date = args[6]

    def add_sale(self):
        sql = ("""INSERT INTO sales_table(attendantid,attendantname,productid,productname,
        productquantity,Total,saledate) VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(self.attedt_id,\
        self.attedt_name,self.product_id,self.product_name,self.product_quantity,self.Total,self.sale_date))
        db_handler().cursor.execute(sql)