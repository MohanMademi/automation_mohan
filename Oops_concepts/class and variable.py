
# HOW TO USE CLASS AND VARIABLES:
class Amazon:
    discount = 5
    def __init__(self,id,name,price,discount):
        self.id = id
        self.nsme =name
        self.price = price
        self.discount = discount

    def actual_price(self):
        final_price = self.price-self.price*self.discount/100-Amazon.discount-self.price/100
        return final_price

v1 = Amazon(1,"shirt",1000,10)
print(v1.actual_price())