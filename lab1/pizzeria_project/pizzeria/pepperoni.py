from .pizza import Pizza

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__(dough="thick", sauce="spicy", toppings=["pepperoni", "cheese", "tomatoes"])
    
    def calculate_price(self):
        return 250
