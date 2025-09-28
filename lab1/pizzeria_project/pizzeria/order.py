class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_cost(self):
        return sum(pizza.price for pizza in self.pizzas)

    def show_order(self):
        print("Preparing your order:")
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
            print(pizza)
