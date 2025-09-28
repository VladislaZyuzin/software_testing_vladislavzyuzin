from .pizza import Pizza

class Seafood(Pizza):
    def __init__(self):
        super().__init__(dough="thin", sauce="white", toppings=["shrimp", "scallops", "cheese"])
    
    def calculate_price(self):
        return 400
