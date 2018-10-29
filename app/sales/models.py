
class Sale:
    """
    Class for creating the sale object

    :params  attedt_id, attedt_name, product_name, product_quantity, product_price, Total, sale_date:
    """
    def __init__(self,*args,**kwargs):
        self.attedt_id = args[0]
        self.attedt_name = args[1]
        self.product_name = args[2]
        self.product_quantity = args[3]
        self.product_price = args[4]
        self.Total = args[5]
        self.sale_date = args[6]

    def to_dict(self):
        """
        Method converts the Sale class instance variables 
        to a dictionary and returns them
        """
        return dict(
                attedt_id = self.attedt_id,
                attedt_name = self.attedt_name,
                product_name = self.product_name,
                product_quantity = self.product_quantity,
                product_price = self.product_price,
                Total = self.Total,
                sale_date = self.sale_date

        )