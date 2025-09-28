class Pizza:
    def __init__(self, dough="thin", sauce="tomato", toppings=None):
        if toppings is None:
            toppings = []
        self._dough = dough
        self._sauce = sauce
        self._toppings = toppings
        self._price = self.calculate_price()

    @property
    def dough(self):
        return self._dough

    @property
    def sauce(self):
        return self._sauce

    @property
    def toppings(self):
        return self._toppings

    @property
    def price(self):
        return self._price

    def prepare(self):
        print(f"Preparing {self.__class__.__name__}:")
        print(f" - Kneading the {self._dough} dough.")
        print(f" - Adding {self._sauce} sauce.")
        print(f" - Adding toppings: {', '.join(self._toppings)}.")
        print(f"Total price: {self._price} rubles.")
        return self._price

    def bake(self):
        print(f"Baking {self.__class__.__name__} in the oven...")

    def cut(self):
        print(f"Cutting {self.__class__.__name__} into slices.")

    def box(self):
        print(f"Boxing {self.__class__.__name__}.")

    def __add__(self, other):
        if isinstance(other, Pizza):
            return Pizza(toppings=self._toppings + other.toppings)
        return NotImplemented

    def __str__(self):
        return f"{self.__class__.__name__} with {self._dough} dough, {self._sauce} sauce and toppings: {', '.join(self._toppings)} is ready."

    def calculate_price(self):
        base_price = 100
        dough_price = 20 if self._dough == "thick" else 0
        sauce_price = 10
        toppings_price = len(self._toppings) * 15
        return base_price + dough_price + sauce_price + toppings_price
