import uuid

class Sale:
    def __init__(self,*args,**kwargs):
        self.sale_id = uuid.uuid4()
        self.attedt_id = args[0]
        self.attedt_name = args[1]
        self.product_name = args[2]
        self.product_quantity = args[3]
        self.product_price = args[4]
        self.Total = args[5]
        self.sale_date = args[6]

    def to_dict(self):
        return dict(
                sale_id = str(self.sale_id.int)[:5],
                attedt_id = self.attedt_id,
                attedt_name = self.attedt_name,
                product_name = self.product_name,
                product_quantity = self.product_quantity,
                product_price = self.product_price,
                Total = self.Total,
                sale_date = self.sale_date

        )