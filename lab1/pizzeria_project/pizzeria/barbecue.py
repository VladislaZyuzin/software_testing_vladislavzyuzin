from .pizza import Pizza

class Barbecue(Pizza):
    def __init__(self):
        super().__init__(dough="thin", sauce="barbecue", toppings=["chicken", "onions", "cheese"])
    
    def calculate_price(self):
        return 300
