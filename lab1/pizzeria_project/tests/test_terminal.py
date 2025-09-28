import pytest
from unittest.mock import patch, MagicMock
from pizzeria.terminal import Terminal
from pizzeria.pepperoni import Pepperoni

class TestTerminal:
    """Тесты для класса Terminal"""
    
    def test_terminal_initialization(self):
        # Arrange & Act
        terminal = Terminal()
        
        # Assert
        assert terminal.order is not None
        assert len(terminal.order.pizzas) == 0

    @patch('builtins.input', side_effect=['1', '4', '5'])
    @patch('builtins.print')
    def test_terminal_take_order_pepperoni(self, mock_print, mock_input):
        # Arrange
        terminal = Terminal()
        
        # Act
        terminal.take_order()
        
        # Assert
        assert len(terminal.order.pizzas) == 1
        assert isinstance(terminal.order.pizzas[0], Pepperoni)

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_terminal_exit_immediately(self, mock_print, mock_input):
        # Arrange
        terminal = Terminal()
        
        # Act
        terminal.take_order()
        
        # Assert
        assert len(terminal.order.pizzas) == 0

    def test_terminal_show_menu_no_errors(self):
        # Arrange
        terminal = Terminal()
        
        # Act & Assert
        try:
            terminal.show_menu()
            assert True
        except Exception:
            assert False, "show_menu should execute without errors"
