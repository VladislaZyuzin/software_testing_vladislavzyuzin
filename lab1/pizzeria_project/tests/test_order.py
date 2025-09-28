import pytest
from pizzeria.order import Order
from pizzeria.pepperoni import Pepperoni
from pizzeria.barbecue import Barbecue

class TestOrder:
    """Тесты для класса Order"""
    
    def test_order_creation_empty(self):
        # Arrange & Act
        order = Order()
        
        # Assert
        assert order.pizzas == []
        assert order.total_cost() == 0

    def test_order_add_pizza(self):
        # Arrange
        order = Order()
        pepperoni = Pepperoni()
        
        # Act
        order.add_pizza(pepperoni)
        
        # Assert
        assert len(order.pizzas) == 1
        assert order.pizzas[0] == pepperoni

    def test_order_total_cost_single_pizza(self):
        # Arrange
        order = Order()
        pepperoni = Pepperoni()
        
        # Act
        order.add_pizza(pepperoni)
        total = order.total_cost()
        
        # Assert
        assert total == 250

    def test_order_total_cost_multiple_pizzas(self):
        # Arrange
        order = Order()
        pepperoni = Pepperoni()
        barbecue = Barbecue()
        
        # Act
        order.add_pizza(pepperoni)
        order.add_pizza(barbecue)
        total = order.total_cost()
        
        # Assert
        assert total == 550  # 250 + 300

    def test_order_show_order_no_errors(self):
        # Arrange
        order = Order()
        pepperoni = Pepperoni()
        order.add_pizza(pepperoni)
        
        # Act & Assert
        # Проверяем, что метод выполняется без ошибок
        try:
            order.show_order()
            assert True
        except Exception:
            assert False, "show_order should execute without errors"
