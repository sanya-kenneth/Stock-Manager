class sale:
    def __init__(self,attedt_id,attedt_name,product_name,product_quantity,product_price,Total,sale_date):
        self.attedt_id = attedt_id
        self.attedt_name = attedt_name
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.Total = Total
        self.sale_date = sale_date

    def to_dict(self):
        return dict(
                attedt_id = self.attedt_id,
                attedt_name = self.attedt_name,
                product_name = self.product_name,
                product_quantity = self.product_quantity,
                product_price = self.product_price,
                Total = self.Total,
                sale_date = self.sale_date

        )