import pytest
from pizzeria.pizza import Pizza
from pizzeria.pepperoni import Pepperoni
from pizzeria.barbecue import Barbecue
from pizzeria.seafood import Seafood

class TestPizza:
    """Тесты для базового класса Pizza"""
    
    def test_pizza_creation_default(self):
        # Arrange
        # Act
        pizza = Pizza()
        
        # Assert
        assert pizza.dough == "thin"
        assert pizza.sauce == "tomato"
        assert pizza.toppings == []
        assert pizza.price == 110  # 100 + 0 + 10 + 0

    def test_pizza_creation_custom(self):
        # Arrange
        toppings = ["cheese", "mushrooms"]
        
        # Act
        pizza = Pizza(dough="thick", sauce="garlic", toppings=toppings)
        
        # Assert
        assert pizza.dough == "thick"
        assert pizza.sauce == "garlic"
        assert pizza.toppings == toppings
        assert pizza.price == 160  # 100 + 20 + 10 + 30

    def test_pizza_prepare_return_price(self):
        # Arrange
        pizza = Pizza()
        
        # Act
        result = pizza.prepare()
        
        # Assert
        assert result == 110

    def test_pizza_add_operation(self):
        # Arrange
        pizza1 = Pizza(toppings=["cheese"])
        pizza2 = Pizza(toppings=["mushrooms"])
        
        # Act
        combined_pizza = pizza1 + pizza2
        
        # Assert
        assert combined_pizza.toppings == ["cheese", "mushrooms"]

    def test_pizza_string_representation(self):
        # Arrange
        pizza = Pizza(dough="thick", sauce="tomato", toppings=["cheese"])
        
        # Act
        result = str(pizza)
        
        # Assert
        assert "Pizza with thick dough, tomato sauce" in result
        assert "cheese" in result

class TestPizzaSubclasses:
    """Тесты для конкретных видов пицц"""
    
    def test_pepperoni_creation(self):
        # Arrange & Act
        pepperoni = Pepperoni()
        
        # Assert
        assert pepperoni.dough == "thick"
        assert pepperoni.sauce == "spicy"
        assert "pepperoni" in pepperoni.toppings
        assert pepperoni.price == 250

    def test_barbecue_creation(self):
        # Arrange & Act
        barbecue = Barbecue()
        
        # Assert
        assert barbecue.dough == "thin"
        assert barbecue.sauce == "barbecue"
        assert "chicken" in barbecue.toppings
        assert barbecue.price == 300

    def test_seafood_creation(self):
        # Arrange & Act
        seafood = Seafood()
        
        # Assert
        assert seafood.dough == "thin"
        assert seafood.sauce == "white"
        assert "shrimp" in seafood.toppings
        assert seafood.price == 400

    def test_different_pizza_prices(self):
        # Arrange
        pepperoni = Pepperoni()
        barbecue = Barbecue()
        seafood = Seafood()
        
        # Act & Assert
        assert pepperoni.price == 250
        assert barbecue.price == 300
        assert seafood.price == 400
        assert seafood.price > barbecue.price > pepperoni.price
